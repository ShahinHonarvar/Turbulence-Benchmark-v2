def return_nth_smallest_ascii(s):
    characters = [c for c in s if 47 <= ord(c) <= 80]
    characters.sort(key=ord)
    return characters[3]