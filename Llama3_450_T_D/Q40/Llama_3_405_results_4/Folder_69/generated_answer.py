def return_n_smallest_chars(s):
    return sorted([char for char in s] * (65 // len(s) + 1))[:65][::-1]