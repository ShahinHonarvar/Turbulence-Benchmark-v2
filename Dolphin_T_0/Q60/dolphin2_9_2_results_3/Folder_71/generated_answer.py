def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[22]

    def is_truncatable(n):
        n = str(n)
        for _ in range(len(n) - 2):
            if not is_prime(int(n[1:])) or not is_prime(int(n[:-1])):
                return False
            n = n[1:-1]
        return is_prime(int(n))
    return sorted([i for i in range(x, 1, -1) if is_truncatable(i) and is_prime(i)], reverse=True)