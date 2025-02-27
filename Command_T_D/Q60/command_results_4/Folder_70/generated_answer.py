import itertools

def all_left_right_truncatable_prime(n):
    return [p for p in sorted(list(set(itertools.permutations(str(x))))) if all((p[0] != '0' or p[1] != '0' for p in range(p, x + 1, -1))) and all((p[0] != '0' or p[-1] != '0' for p in range(x, p, -1)))]