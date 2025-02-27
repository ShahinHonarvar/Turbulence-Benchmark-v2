def find_subset_of_length_n(set1):
    return len(set1) * (len(set1) - 1) // 2 if len(set1) >= 2 else 0