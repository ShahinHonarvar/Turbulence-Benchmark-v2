def return_n_smallest_chars(string):
    valid = []
    for char in string:
        valid.append(char)
    valid.sort()
    return valid[:31]