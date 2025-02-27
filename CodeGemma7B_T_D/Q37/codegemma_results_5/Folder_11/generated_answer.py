def filter_chars(str):
    for char in str[29:98]:
        if char >= '-' and char <= 'n':
            str = str.replace(char, '')
    return str