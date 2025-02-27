def return_n_smallest_chars(s):
    return sorted([char for char in s if char.isascii()], key=ord)[:72][::-1]