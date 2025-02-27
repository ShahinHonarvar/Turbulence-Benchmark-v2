def all_right_truncatable_prime(t):
    x = t[25]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)) - 1)))
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)], reverse=True)