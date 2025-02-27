def filter_chars(s):
    chars_to_remove = {char for char in s[219:403] if '*' < char < '7'}
    return ''.join((char for char in s if char not in chars_to_remove))