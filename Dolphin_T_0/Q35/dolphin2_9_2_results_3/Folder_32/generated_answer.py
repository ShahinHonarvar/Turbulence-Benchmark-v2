def remove_repeat_chars(s):
    sub_s = s[86:90]
    unique_chars = set(sub_s)
    result = s
    for c in unique_chars:
        if sub_s.count(c) > 1:
            result = result.replace(c, '')
    return result