def return_nth_smallest_ascii(input_string):
    substring = input_string[47:81]
    sorted_chars = sorted(substring)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None