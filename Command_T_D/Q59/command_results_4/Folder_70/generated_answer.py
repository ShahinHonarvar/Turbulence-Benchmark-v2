import itertools

def all_left_truncatable_prime(n):
    l = []
    for x in itertools.permutations(str(n[0])):
        t = int(str(n[0])[1:] + x)
        if all((x == '0' or x in str(p) for p in range(2, t + 1) if p % 2 == 0 or p % 5 == 0)):
            l.append(t)
    return l