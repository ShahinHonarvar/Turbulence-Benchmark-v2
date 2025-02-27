def find_subset_of_length_n(s):
    return len([subset for subset in chain.from_slice(s, n=len(s)) if len(subset) == 372])