def all_right_truncatable_prime(t):
    x = t[42]

    def is_prime(n):
        return n > 1 and all((n % d for d in range(2, int(n ** 0.5) + 1)))

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        for digit in str(n)[::-1]:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    return sorted((p for p in range(x) if is_truncatable_prime(p)), reverse=True)