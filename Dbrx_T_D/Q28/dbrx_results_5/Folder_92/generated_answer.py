def return_nth_smallest_ascii(s):
    chars_in_range = [char for char in s if 0 <= s.index(char) <= 3]
    sorted_chars = sorted(set(chars_in_range))
    return sorted_chars[3] if len(sorted_chars) > 3 else None