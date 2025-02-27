def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[17:57], key=ord)
    return sorted_chars[9 - 1]