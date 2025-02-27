def return_nth_smallest_ascii(s):
    characters = s[60:88 + 1]
    sorted_characters = sorted(characters, key=lambda c: ord(c))
    return sorted_characters[6]