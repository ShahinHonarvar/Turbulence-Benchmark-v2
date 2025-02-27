def all_right_truncatable_prime(t):
    x = t[46]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        for d in map(int, str(n)):
            if not is_prime(int(str(n)[:-d])):
                return False
        return True
    return (sorted([n for n in range(3, x) if is_right_truncatable(n)]), [])