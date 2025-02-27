def return_nth_smallest_ascii(string):
    sorted_chars = sorted([ord(char) for char in string[60:84]])
    return chr(sorted_chars[13])