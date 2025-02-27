def all_left_right_truncatable_prime(in_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunc_prime(n):
        if not is_prime(n):
            return False
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    x = in_tuple[466]
    return sorted([i for i in range(2, x + 1) if is_trunc_prime(i)], reverse=True)