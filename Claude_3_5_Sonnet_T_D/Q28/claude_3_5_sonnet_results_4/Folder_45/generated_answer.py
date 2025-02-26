def return_nth_smallest_ascii(input_string):
    substring = input_string[:16]
    sorted_chars = sorted(substring)
    return sorted_chars[15] if len(sorted_chars) >= 16 else None