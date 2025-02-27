def all_right_truncatable_prime(lst):
    x = lst[35]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunkatable(n):
        n_str = str(n)
        for i in range(len(n_str) - 1, 0, -1):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if is_prime(n) and is_trunkatable(n)], reverse=True)