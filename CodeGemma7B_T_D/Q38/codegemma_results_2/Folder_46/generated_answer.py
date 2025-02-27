def find_powerset(a):
    return 2 ** len(a)

def find_subset_of_length_n(set, n):
    return find_powerset(set) // 2 ** (len(set) - n)