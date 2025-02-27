def remove_repeat_chars(s):
    sub_str = s[82:86]
    repeated_chars = {ch for ch in set(sub_str) if sub_str.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in repeated_chars or s.index(ch) < 82 or s.index(ch) > 85))