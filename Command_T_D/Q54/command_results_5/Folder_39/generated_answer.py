import itertools

def all_right_truncatable_prime(test_tuple):
    res = list(filter(lambda x: is_right_truncatable_prime(x), list(range(test_tuple[30]))))
    return res

def is_right_truncatable_prime(n):
    return all((n % d != 0 for d in range(2, int(str(n)[-1]) + 1)))