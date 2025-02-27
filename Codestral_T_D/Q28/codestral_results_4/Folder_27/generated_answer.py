def return_nth_smallest_ascii(string):
    valid_chars = [c for c in string if 33 <= ord(c) <= 85]
    sorted_chars = sorted(valid_chars, key=ord)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    else:
        return None