def all_left_truncatable_prime(tuple):
    x = tuple[84]
    is_prime = lambda n: all((i % n != 0 for i in range(2, int(n ** 0.5) + 1)))
    letrun = lambda n, digits: all((i in digits for i in str(n).lstrip('0'))) and len(str(n).lstrip('0')) > 2
    x_list = list(range(x))
    result = sorted([i for i in x_list if letrun(i, tuple) and is_prime(i)], reverse=True)
    return result