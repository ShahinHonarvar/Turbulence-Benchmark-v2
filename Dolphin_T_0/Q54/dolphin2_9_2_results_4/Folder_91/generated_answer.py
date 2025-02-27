def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num = n
        while num != 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    x = t[0]
    lst = [i for i in range(x - 1, 1, -1) if is_right_truncatable(i)]
    return sorted(lst, reverse=True)