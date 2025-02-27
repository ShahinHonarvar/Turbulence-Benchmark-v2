def find_subset_of_length_n(elements):
    n = 76
    return len([subset for subset in powerset(elements) if len(subset) == n])

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield set((s[j] for j in range(x) if masks[j] & i))