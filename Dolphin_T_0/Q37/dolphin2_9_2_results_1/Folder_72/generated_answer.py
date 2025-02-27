def filter_chars(string):
    for char in range(35, 52):
        for ch in range(ord(string[char]), ord(string[char]) // 2 + 26):
            string = string.replace(chr(ch), '', 2)
    return string