import itertools

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[43]
    return sorted(set(filter(lambda x: all((x % d for d in range(2, int(x ** 0.5) + 1))), list(map(str, itertools.permutations(range(2, int(x ** 0.5) + 1)))))))