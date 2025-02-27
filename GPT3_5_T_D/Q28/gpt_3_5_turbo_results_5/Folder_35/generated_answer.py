def return_nth_smallest_ascii(string):
    substring = string[50:76]
    sorted_chars = sorted(set(substring))
    return sorted_chars[6]