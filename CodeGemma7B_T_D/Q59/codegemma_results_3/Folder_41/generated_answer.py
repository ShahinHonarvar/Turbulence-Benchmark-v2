def all_left_truncatable_prime(x_tuple):
    not_zero = lambda x: not str(x).startswith('0')
    all_prime = lambda x: all((num in primerange(2, int(x ** (1 / 2)) + 1) if num in x else True for num in str(x)))
    x = x_tuple[46]
    res = [i for i in range(x) if all_prime(i) if not_zero(i)]
    return sorted(res, reverse=True)