def all_left_truncatable_prime(num_tuple):
    x = num_tuple[14]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def left_truncate(n):
        if n < 10:
            return []
        return [int(str(n)[:i]) for i in range(len(str(n)) - 1, 0, -1)]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all((is_prime(i) for i in left_truncate(n)))
    return sorted((i for i in range(2, x) if is_left_truncatable_prime(i)))