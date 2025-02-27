def all_right_truncatable_prime(args):
    x = args[26]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    right_truncatable = []
    for i in range(2, x):
        if is_prime(i):
            if all((is_prime(int(str(i)[:-j]) if str(i)[:-j] else 1) for j in range(1, len(str(i))))):
                right_truncatable.append(i)
    return sorted(right_truncatable)