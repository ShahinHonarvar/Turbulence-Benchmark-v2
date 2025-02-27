def return_nth_smallest_ascii(s):
    if len(s) < 65:
        return None
    characters = list(s[25:65])
    characters.sort(key=lambda c: ord(c))
    return characters[5] if len(characters) >= 6 else None