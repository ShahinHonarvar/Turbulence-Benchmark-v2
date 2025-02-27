def all_right_truncatable_prime(t):
    if t[54] < 2 or t[54] % 2 == 0:
        return []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    result = []
    for i in range(t[54] - 1, 2, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)