def return_n_smallest_chars(s):
    return sorted([char for char in s if s.index(char) < 43], reverse=True)