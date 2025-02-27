def return_nth_smallest_ascii(string):
    if len(string) < 10:
        return None
    limited_string = string[:10]
    sorted_chars = sorted(limited_string)
    return sorted_chars[9]