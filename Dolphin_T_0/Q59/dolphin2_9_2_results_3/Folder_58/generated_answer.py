def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[975]
    return sorted([i for i in range(x, 1, -1) if is_prime(i) and all((is_prime(int(str(i)[1:])) for _ in range(len(str(i)) - 1)))], reverse=True)