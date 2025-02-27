def all_left_truncatable_prime(t):
    x = t[71]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_prime(i) and left_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)