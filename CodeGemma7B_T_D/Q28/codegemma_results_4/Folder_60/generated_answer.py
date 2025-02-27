def return_nth_smallest_ascii(s):
    characters = list(s[36:80])
    characters.sort(key=ord)
    return characters[11]