def return_nth_smallest_ascii(string):
    substring = string[20:81]
    sorted_chars = sorted(set(substring))
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    return None