def return_nth_smallest_ascii(string):
    return sorted([ch for ch in string if string.index(ch) in range(1, 32)])[5]