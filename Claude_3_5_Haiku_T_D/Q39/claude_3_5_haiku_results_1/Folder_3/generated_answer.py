def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string), key=lambda x: ord(x), reverse=True)
    return sorted_chars[:28]