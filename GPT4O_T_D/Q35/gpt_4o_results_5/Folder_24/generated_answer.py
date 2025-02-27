def remove_repeat_chars(s):
    if len(s) <= 15:
        return s
    sub_string = s[14:91]
    removal_set = {ch for ch in sub_string if sub_string.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in removal_set or s.index(ch) <= 13 or s.index(ch) >= 91))