def return_nth_smallest_ascii(string):
    chars = string[0:10]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[9]