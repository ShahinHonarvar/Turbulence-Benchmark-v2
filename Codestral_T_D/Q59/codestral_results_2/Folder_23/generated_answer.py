def all_left_truncatable_prime(input_tuple):
    x = input_tuple[77]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncate(n):
        return [int(n[i:]) for i in range(1, len(n))]

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        return all((is_prime(x) for x in left_truncate(str(n))))
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)