def return_nth_smallest_ascii(string):
    substring = string[14:67]
    unique_chars = list(set(substring))
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) < 8:
        return None
    else:
        return sorted_chars[8]