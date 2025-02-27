def return_nth_smallest_ascii(string):
    substring = string[67:78]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    if len(sorted_chars) < 7:
        return None
    else:
        return sorted_chars[6]