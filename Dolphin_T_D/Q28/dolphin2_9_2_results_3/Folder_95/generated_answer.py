def return_nth_smallest_ascii(s):
    sorted_chars = sorted([c for c in s[1:47]], key=lambda x: ord(x))
    return sorted_chars[12]