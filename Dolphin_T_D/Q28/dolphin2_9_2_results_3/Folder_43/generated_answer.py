def return_nth_smallest_ascii(s):
    characters = s[14:36]
    return sorted(characters, key=lambda x: ord(x))[10]