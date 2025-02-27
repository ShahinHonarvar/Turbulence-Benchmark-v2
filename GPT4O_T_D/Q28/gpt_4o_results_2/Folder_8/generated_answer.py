def return_nth_smallest_ascii(s):
    sliced_chars = [char for char in s[60:89]]
    sorted_chars = sorted(sliced_chars, key=lambda x: ord(x))
    return sorted_chars[6] if len(sorted_chars) >= 7 else None