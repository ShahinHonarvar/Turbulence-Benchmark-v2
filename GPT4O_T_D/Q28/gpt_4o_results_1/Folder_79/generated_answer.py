def return_nth_smallest_ascii(s):
    if len(s) < 36:
        return None
    characters = s[13:36]
    sorted_chars = sorted(characters)
    if len(sorted_chars) < 18:
        return None
    return sorted_chars[17]