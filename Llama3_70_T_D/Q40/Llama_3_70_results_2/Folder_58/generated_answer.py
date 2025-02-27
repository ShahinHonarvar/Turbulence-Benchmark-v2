def return_n_smallest_chars(s):
    return sorted([char for char in s if ord(char) < 49], reverse=True)[:49]