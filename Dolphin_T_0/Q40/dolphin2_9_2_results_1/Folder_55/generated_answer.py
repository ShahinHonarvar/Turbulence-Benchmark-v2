def return_n_smallest_chars(string):
    chars = [char for char in string]
    chars.sort(reverse=True)
    return chars[:75]