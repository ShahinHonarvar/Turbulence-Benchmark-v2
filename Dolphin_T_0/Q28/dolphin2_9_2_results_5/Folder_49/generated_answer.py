def return_nth_smallest_ascii(s):
    s = s[20:81]
    characters = list(s)
    characters.sort(key=lambda x: ord(x))
    return characters[10]