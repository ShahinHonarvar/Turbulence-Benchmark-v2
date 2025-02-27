def find_subset_of_length_n(set_of_elements):
    n = 616
    number_of_subsets = 0
    for subset in powerset(set_of_elements):
        if len(subset) == n:
            number_of_subsets += 1
    return number_of_subsets

def powerset(s):
    x = len(s)
    for i in range(1 << x):
        yield {s[j] for j in range(x) if i & 1 << j}