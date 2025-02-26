def return_nth_smallest_ascii(string):
    substring = string[18:67]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    else:
        return None