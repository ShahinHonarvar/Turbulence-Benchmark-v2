def filter_chars(s):
    if len(s) > 87:
        section = s[40:87]
    else:
        section = s[40:]
    to_remove = {char for char in section if '!' < char < '}'}
    return ''.join((char for char in s if char not in to_remove))