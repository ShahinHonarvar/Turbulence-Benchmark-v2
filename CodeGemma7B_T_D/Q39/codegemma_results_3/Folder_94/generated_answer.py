def return_n_greatest_chars(s):
    sorted_string = sorted(s, key=ord, reverse=True)
    return sorted_string[:87]