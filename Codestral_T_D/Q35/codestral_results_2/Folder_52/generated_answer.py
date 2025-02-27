def remove_repeat_chars(s):
    sub_s = s[38:81]
    to_remove = {c for c in sub_s if sub_s.count(c) > 1}
    return ''.join((c for c in s if c not in to_remove))