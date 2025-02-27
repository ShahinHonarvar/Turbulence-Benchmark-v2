def return_nth_smallest_ascii(string):
    substring = string[9:59]
    sorted_chars = sorted(substring, key=lambda ch: ord(ch))
    return sorted_chars[5]