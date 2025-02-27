def filter_chars(s):
    char_list = [char for char in s]
    for i in range(46, 91):
        if chr(i) > 'D' and chr(i) < 'H':
            while chr(i) in char_list:
                char_list.remove(chr(i))
    return ''.join(char_list)