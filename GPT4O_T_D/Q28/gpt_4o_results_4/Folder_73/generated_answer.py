def return_nth_smallest_ascii(s):
    limited_chars = s[:70]
    sorted_characters = sorted(limited_chars)
    if len(sorted_characters) >= 10:
        return sorted_characters[9]
    return None