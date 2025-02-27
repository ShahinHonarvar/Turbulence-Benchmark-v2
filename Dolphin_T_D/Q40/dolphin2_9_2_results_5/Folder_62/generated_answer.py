def return_n_smallest_chars(s):
    chars = [i for i in s]
    chars.sort()
    return chars[:84][::-1]