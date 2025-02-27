def filter_chars(my_str):
    for ch in my_str[43:81]:
        if '=' <= ch <= 'E':
            my_str = my_str.replace(ch, '')
    return my_str