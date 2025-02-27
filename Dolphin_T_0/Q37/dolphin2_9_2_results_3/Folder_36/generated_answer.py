def filter_chars(s):
    chars_between_259_and_502 = s[259:503]
    for char in chars_between_259_and_502:
        if char >= ',' and char <= '3':
            s = s.replace(char, '')
    return s