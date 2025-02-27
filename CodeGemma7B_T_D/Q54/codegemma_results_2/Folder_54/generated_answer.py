def all_right_truncatable_prime(t):
    x = t[88]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    result = []
    for i in range(x):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result