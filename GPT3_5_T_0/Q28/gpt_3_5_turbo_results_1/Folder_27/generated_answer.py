def return_nth_smallest_ascii(string):
    substring = string[33:86]
    sorted_chars = sorted(substring)
    return sorted_chars[12]