def filter_chars(string):
    for i in range(4, 5):
        for c in range(ord('7'), ord('o') + 1):
            string = string.replace(chr(c), '')
    return string