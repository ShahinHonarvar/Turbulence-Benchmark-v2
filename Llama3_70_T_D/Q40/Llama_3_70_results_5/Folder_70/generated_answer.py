def return_n_smallest_chars(s):
    if len(s) < 2:
        return []
    return sorted([min(s), sorted([char for char in s if char != min(s)])[0]], reverse=True)