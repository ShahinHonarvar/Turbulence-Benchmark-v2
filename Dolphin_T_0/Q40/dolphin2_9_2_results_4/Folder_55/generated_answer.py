def return_n_smallest_chars(s):
    return sorted([char for char in s], key=lambda x: ord(x), reverse=True)[:75]