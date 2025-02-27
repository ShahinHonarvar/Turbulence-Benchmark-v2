def return_nth_smallest_ascii(s):
    substring = s[:19]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    return sorted_chars[12]