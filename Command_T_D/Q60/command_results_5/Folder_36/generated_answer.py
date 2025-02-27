import itertools

def all_left_right_truncatable_prime(n):
    if n == (10, 10 ** 5):
        return []
    for p in itertools.permutations(str(n[0]) + str(n[1]), 2):
        if p[0] != '0' and p[1] != '0' and (int(p[0]) <= n[0]) and (int(p[1]) <= n[1]):
            yield int(p[0])
            yield int(p[1])