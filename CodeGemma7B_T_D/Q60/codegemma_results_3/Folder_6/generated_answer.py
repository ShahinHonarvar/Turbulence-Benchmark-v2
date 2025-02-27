def all_left_right_truncatable_prime(s):
    x = s[74]
    results = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    def is_right_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    for i in range(2, x + 1):
        if is_prime(i) and is_left_prime(i) and is_right_prime(i):
            results.append(i)
    return sorted(results)