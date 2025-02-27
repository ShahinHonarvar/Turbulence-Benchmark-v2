def return_n_smallest_chars(string):
    chars = [char for char in string]
    chars.sort(key=lambda x: ord(x))
    chars = chars[:27]
    chars.sort(reverse=True)
    return chars