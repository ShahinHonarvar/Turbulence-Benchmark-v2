def return_nth_smallest_ascii(string):
    string = string[51:61]
    sorted_chars = sorted(string, key=lambda x: ord(x))
    return sorted_chars[4]