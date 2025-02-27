def return_nth_smallest_ascii(string):
    string = string[28:55]
    unique_chars = list(set(string))
    unique_chars.sort()
    return unique_chars[13]