def return_nth_smallest_ascii(string):
    substring = string[48:77]
    sorted_chars = sorted(substring)
    return sorted_chars[4]