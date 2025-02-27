def return_n_greatest_chars(test_string):
    sorted_chars = sorted(test_string, key=lambda c: -ord(c))
    return sorted(sorted_chars[:5])