def return_n_smallest_chars(s):
    return sorted([char for char in s] + [min(s)] * (32 - len(s)), reverse=True)[:32]