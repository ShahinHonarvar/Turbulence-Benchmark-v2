def all_right_truncatable_prime(t):
    x = t[370]

    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_r_truncatable(n):
        return all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    return sorted([n for n in range(2, x) if is_prime(n) and is_r_truncatable(n)], reverse=True) or []