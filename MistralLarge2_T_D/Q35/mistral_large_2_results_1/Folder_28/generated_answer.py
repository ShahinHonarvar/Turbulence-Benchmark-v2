def remove_repeat_chars(s):
    sub = s[86:99]
    to_remove = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))