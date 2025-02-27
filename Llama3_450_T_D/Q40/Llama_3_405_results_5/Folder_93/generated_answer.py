def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda x: ord(x))
    seventy_seven_smallest = ascii_sorted[:77]
    return sorted(seventy_seven_smallest, reverse=True)