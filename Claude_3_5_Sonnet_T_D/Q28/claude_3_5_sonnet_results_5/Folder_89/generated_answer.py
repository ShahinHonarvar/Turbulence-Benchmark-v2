def return_nth_smallest_ascii(input_string):
    substring = input_string[24:72]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 8:
        return sorted_chars[7]
    else:
        return None