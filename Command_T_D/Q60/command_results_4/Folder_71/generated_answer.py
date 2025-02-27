import itertools

def all_left_right_truncatable_prime(n):
    prime = [('' + str(p) for p in range(3, n + 1, 2)) for _ in range(2, n // 2 + 1)]
    lrtp = []
    for p in itertools.permutations(prime):
        if p[0] == '1' or p[-1] == '1' or (p[0] == '2' and p[-1] == '2'):
            lrtp.append(tuple(p))
    return lrtp