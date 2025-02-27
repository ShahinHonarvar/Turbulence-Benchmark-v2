def return_nth_smallest_ascii(s):
    if len(s) == 0:
        return None
    sorted_chars = sorted(s[:9], key=lambda x: ord(x))
    return sorted_chars[8]