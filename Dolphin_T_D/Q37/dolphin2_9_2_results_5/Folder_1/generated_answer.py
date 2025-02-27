def filter_chars(string):
    sub_string = string[41:80]
    string_list = list(string)
    for char in sub_string:
        if 'f' <= char <= '|':
            string_list = [i for i in string_list if i != char]
    return ''.join(string_list)