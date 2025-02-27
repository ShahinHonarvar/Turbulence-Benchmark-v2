def find_subset_of_length_n(input_set):
    total_subsets = 0
    for subset in powerset(input_set):
        if len(subset) == 36:
            total_subsets += 1
    return total_subsets

def powerset(s):
    for i in range(1 << len(s)):
        yield set([s[j] for j in range(len(s)) if i & 1 << j])