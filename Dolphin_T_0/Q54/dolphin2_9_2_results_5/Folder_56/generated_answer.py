def all_right_truncatable_prime(lst):
    x = lst[30]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[-1])
        return True
    return sorted({n for n in range(2, x) if is_truncatable(n)})