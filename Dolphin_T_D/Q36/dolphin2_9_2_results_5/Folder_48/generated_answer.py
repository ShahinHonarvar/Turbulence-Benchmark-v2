def filter_chars(string):
    string_list = list(string)
    for char in string[154:222]:
        if 'A' < char < 'f':
            string_list = [c for c in string_list if c != char]
    return ''.join(string_list)