def return_nth_smallest_ascii(string):
    substring = string[22:75]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 12:
        return sorted_chars[11]
    else:
        return None