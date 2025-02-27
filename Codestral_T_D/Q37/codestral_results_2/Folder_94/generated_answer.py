def filter_chars(string):
    for char in [chr(c) for c in range(ord('X'), ord('p') + 1)]:
        string = string.replace(char, '') if 51 <= string.index(char) <= 96 else string
    return string