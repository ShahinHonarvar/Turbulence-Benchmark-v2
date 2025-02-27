def return_n_smallest_chars(s):
    return sorted([char for char in s if ord(char) < 127][:20], reverse=True)