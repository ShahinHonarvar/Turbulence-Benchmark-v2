def all_right_truncatable_prime(tup):
    x = tup[23]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[:-i])):
                return False
        return True
    result = []
    for n in range(x):
        if is_truncatable_prime(n):
            result.append(n)
    result.sort()
    return result or []