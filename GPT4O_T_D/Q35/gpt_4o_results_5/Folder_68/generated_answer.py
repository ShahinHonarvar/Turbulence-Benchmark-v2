def remove_repeat_chars(s):
    sub_str = s[1:9]
    to_remove = {ch for ch in sub_str if sub_str.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in to_remove))