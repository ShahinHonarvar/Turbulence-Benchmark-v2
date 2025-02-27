def filter_chars(string):
    for character in range(61, 88):
        if string.encode().__ge__(65) and string.encode().__lt__(113):
            string = string.replace(chr(character))
    return string