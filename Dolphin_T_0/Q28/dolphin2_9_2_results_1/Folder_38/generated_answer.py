def return_nth_smallest_ascii(s):
    chars = list(s[:46])
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[9]