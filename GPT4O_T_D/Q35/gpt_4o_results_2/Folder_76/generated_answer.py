def remove_repeat_chars(s):
    if len(s) <= 544:
        return s
    sub_str = s[331:543]
    to_remove = {char for char in sub_str if sub_str.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) <= 330 or s.index(char) >= 543))