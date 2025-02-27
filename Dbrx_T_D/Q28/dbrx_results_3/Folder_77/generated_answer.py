def return_nth_smallest_ascii(string):
    chars_in_range = [char for char in string if 63 <= ord(char) <= 76]
    sorted_chars = sorted(set(chars_in_range))
    if len(sorted_chars) < 14:
        return None
    else:
        return sorted_chars[13]