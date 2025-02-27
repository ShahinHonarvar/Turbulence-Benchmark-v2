def return_n_smallest_chars(s):
    return sorted([char for char in s if len(char) == 1], key=ord, reverse=True)[:45]