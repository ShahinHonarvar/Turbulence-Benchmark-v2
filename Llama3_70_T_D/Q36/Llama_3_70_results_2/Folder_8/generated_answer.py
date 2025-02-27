def filter_chars(s):
    result = ''
    char_list = list(s)
    for char in s[82:93]:
        if '!' < char < '*':
            char_list = [c for c in char_list if c != char]
    return ''.join(char_list)