def return_n_greatest_chars(my_string):
    return sorted([ch for ch in my_string if ch in string.printable][-47:])