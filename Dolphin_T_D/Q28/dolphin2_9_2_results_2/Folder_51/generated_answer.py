def return_nth_smallest_ascii(s):
    characters = s[10:74]
    sorted_characters = sorted(characters, key=lambda x: ord(x))
    return sorted_characters[9]