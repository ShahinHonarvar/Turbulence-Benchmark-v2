def filter_chars(s):
    chars_to_remove = set(s[44:48])
    chars_to_remove = {char for char in chars_to_remove if '+' < char < 'l'}
    s_list = list(s)
    s_list = [char for char in s_list if char not in chars_to_remove]
    return ''.join(s_list)