def return_n_smallest_chars(s):
    return sorted([char for char in s] * (36 // len(s) + 1))[:36][::-1]