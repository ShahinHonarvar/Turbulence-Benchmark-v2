def return_n_smallest_chars(s):
    return sorted([char for char in s if len(set(s)) >= 66][:66], reverse=True)