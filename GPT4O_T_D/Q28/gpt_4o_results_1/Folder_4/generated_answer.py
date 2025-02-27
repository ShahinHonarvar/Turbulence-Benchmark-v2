def return_nth_smallest_ascii(s):
    characters_in_range = s[9:23]
    sorted_characters = sorted(characters_in_range)
    return sorted_characters[3] if len(sorted_characters) >= 4 else None