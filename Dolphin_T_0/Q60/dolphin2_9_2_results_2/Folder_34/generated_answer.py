def all_left_right_truncatable_prime(P):
    x = P[18]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return False
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
                return False
        return True
    L = [i for i in range(2, x + 1) if is_truncatable(i)]
    return sorted(L, reverse=True)