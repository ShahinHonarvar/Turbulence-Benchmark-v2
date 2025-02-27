def return_nth_smallest_ascii(input_string):
    chars_to_consider = [char for char in input_string if 47 <= ord(char) <= 70]
    sorted_chars = sorted(chars_to_consider)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    else:
        return None