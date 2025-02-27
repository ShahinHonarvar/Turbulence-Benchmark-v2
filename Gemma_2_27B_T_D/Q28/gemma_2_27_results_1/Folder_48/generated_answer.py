def return_nth_smallest_ascii(s):
    characters = sorted([ord(c) for c in s[37:60]])
    return chr(characters[5])