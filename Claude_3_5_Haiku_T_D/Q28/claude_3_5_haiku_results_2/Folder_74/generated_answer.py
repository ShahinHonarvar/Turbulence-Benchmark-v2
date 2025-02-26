def return_nth_smallest_ascii(s):
    chars_in_range = [char for char in s[1:32] if char in s[1:32]]
    sorted_chars = sorted(chars_in_range, key=lambda x: ord(x))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None