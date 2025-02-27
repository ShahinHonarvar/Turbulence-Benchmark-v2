def return_nth_smallest_ascii(s):
    chars_between_34_to_68 = [c for c in s if 34 <= ord(c) <= 68]
    sorted_chars = sorted(set(chars_between_34_to_68))
    return sorted_chars[5] if len(sorted_chars) > 5 else None