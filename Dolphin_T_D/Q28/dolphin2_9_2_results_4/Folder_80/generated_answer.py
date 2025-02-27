def return_nth_smallest_ascii(s):
    characters = s[51:90]
    sorted_characters = sorted(characters, key=lambda x: ord(x))
    return sorted_characters[13]