def find_subset_of_length_n(s, n=15):
    if n == 0:
        return [[]]
    if s:
        c = find_subset_of_length_n(s[1:], n - 1)
        return c + [c[i] + [s[0]] for i in range(len(c))]
    else:
        return []

def count_subsets(s):
    subsets = find_subset_of_length_n(s)
    return len(subsets)