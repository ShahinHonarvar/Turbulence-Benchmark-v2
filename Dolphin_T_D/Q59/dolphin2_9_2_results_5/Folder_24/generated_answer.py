def all_left_truncatable_prime(arg):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = arg[65]
    left_truncatable = [str(x) for x in range(x) if is_prime(x) and (not '0' in str(x))]
    left_truncatable = [x for x in left_truncatable if all([is_prime(int(str(x)[i:])) for i in range(1, len(str(x)))] + [x == str(int(x))])]
    return sorted(left_truncatable, key=int, reverse=True)