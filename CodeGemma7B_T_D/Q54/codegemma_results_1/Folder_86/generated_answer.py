def all_right_truncatable_prime(n):

    def is_prime(x):
        if x < 2 or x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def right_truncatable(x):
        for i in range(1, len(str(x))):
            if not is_prime(int(str(x)[:-i])):
                return False
        return True
    ans = []
    for i in n:
        if is_prime(i) and right_truncatable(i):
            ans.append(i)
    return sorted(ans, reverse=True) or []