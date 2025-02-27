def return_nth_smallest_ascii(string):
    substring = string[9:23]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[3]