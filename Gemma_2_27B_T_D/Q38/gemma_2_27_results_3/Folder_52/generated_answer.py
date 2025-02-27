def find_subset_of_length_n(s):
    n = len(s)
    return int(fact(n) / (fact(32) * fact(n - 32)))

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)