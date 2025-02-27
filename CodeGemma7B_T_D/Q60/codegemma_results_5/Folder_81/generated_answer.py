def all_left_right_truncatable_prime(arg):
    x = arg[98]

    def is_prime(n):
        return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def left_right_truncatable(n):
        ndigits = len(str(n))
        for shift in range(1, ndigits):
            right = n % 10 ** (ndigits - shift)
            left = n // 10 ** (ndigits - shift)
            if not is_prime(right + left) or '0' in str(right + left):
                return False
        if not is_prime(n):
            return False
        return True
    result = filter(left_right_truncatable, range(2, x))
    if result:
        return sorted([x for x in result])
    else:
        return []