def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n):
        if n <= 11:
            return n == 2 or n == 3 or n == 5 or (n == 7)
        str_n = str(n)
        return all((is_prime(int(str_n[i:-i])) for i in range(len(str_n) // 2)))
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)])