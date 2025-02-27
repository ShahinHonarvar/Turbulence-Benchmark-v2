def return_nth_smallest_ascii(s):
    characters_in_range = s[40:61]
    sorted_characters = sorted(characters_in_range, key=lambda x: ord(x))
    if len(sorted_characters) >= 19:
        return sorted_characters[18]
    return None