def return_nth_smallest_ascii(string):
    sub_string = string[17:84]
    unique_chars = set(sub_string)
    if len(unique_chars) < 5:
        return None
    sorted_chars = sorted(unique_chars)
    return sorted_chars[4]