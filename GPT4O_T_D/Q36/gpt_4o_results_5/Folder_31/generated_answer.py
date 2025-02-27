def filter_chars(s):
    if len(s) < 75:
        check_range = s[14:-1]
    else:
        check_range = s[14:75]
    filter_set = {char for char in check_range if '9' < char < 'K'}
    return ''.join((char for char in s if char not in filter_set))