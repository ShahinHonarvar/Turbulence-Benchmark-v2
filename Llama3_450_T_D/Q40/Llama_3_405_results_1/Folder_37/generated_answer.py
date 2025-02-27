def return_n_smallest_chars(s):
    return sorted([char for char in s] * (26 // len(s) + 1))[:26][::-1]