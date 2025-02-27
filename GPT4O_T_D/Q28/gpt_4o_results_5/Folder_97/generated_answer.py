def return_nth_smallest_ascii(s):
    characters = s[15:22]
    sorted_characters = sorted(characters, key=lambda x: ord(x))
    return sorted_characters[5] if len(sorted_characters) >= 6 else None