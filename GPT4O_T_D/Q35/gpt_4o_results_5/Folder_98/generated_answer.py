def remove_repeat_chars(s):
    if len(s) < 8:
        return s
    sub_str = s[1:7]
    to_remove = {char for char in sub_str if sub_str.count(char) > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result