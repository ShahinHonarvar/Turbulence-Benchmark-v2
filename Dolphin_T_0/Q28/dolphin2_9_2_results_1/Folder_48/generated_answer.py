def return_nth_smallest_ascii(string):
    substring = string[37:60]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[5]