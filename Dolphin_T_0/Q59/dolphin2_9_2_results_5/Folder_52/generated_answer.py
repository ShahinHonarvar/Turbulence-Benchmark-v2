def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in {0, 1}:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n in {2, 3, 5, 7}:
            return True
        n = str(n)
        while len(n) > 1:
            if n[0] == '0' or not is_prime(int(n)):
                return False
            n = n[1:]
        return is_prime(int(n))
    if len(t) != 2:
        return []
    x = t[1]
    return sorted({int(n) for n in range(2, x) if is_left_truncatable_prime(n)}, reverse=True)