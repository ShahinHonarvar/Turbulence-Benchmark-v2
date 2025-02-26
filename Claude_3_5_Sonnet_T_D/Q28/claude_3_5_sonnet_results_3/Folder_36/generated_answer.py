def return_nth_smallest_ascii(string):
    substring = string[17:57]
    sorted_chars = sorted(substring)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None