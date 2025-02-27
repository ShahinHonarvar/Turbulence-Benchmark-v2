import itertools

def all_left_right_truncatable_prime(x_range):
    if not x_range[94]:
        return []

    def check(x):
        if x <= x_range[94]:
            if all((x % d for d in range(3, int(x ** 0.5) + 1, 2))):
                if not str(x).count('0'):
                    return True
        return False

    def generate(x):
        yield from itertools.permutations(str(x), 2)
        for d in range(2, len(str(x)) + 1):
            if check(x * 10 ** (d - 1)):
                yield from itertools.permutations(str(x * 10 ** (d - 1)), 2)
    return sorted(set(generate(x_range[94])))