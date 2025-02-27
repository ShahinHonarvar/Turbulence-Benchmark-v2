def all_right_truncatable_prime(t):
    x = t[100]

    def is_prime(n):
        if n <= 1:
            return False
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)