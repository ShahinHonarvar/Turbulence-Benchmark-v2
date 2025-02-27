def return_nth_smallest_ascii(s):
    substring = s[33:85]
    characters = list(substring)
    characters.sort(key=lambda x: ord(x))
    return characters[13 - 1]