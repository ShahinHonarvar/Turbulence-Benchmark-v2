def return_nth_smallest_ascii(string):
    subset = string[:19]
    sorted_chars = sorted(subset)
    return sorted_chars[12]