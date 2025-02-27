def return_nth_smallest_ascii(s):
    chars_in_range = [ch for ch in s[:70]]
    sorted_chars = sorted(chars_in_range, key=lambda ch: ord(ch))
    return sorted_chars[9] if len(sorted_chars) >= 10 else None