def filter_chars(string):
    need_filter = string[11:46]
    for char in need_filter:
        if '!' < char < 'A':
            string = string.replace(char, '')
    return string