def filter_chars(s):
    for char in s[219:403]:
        if char > '*' and char < '7':
            s = s.replace(char, '')
    return s