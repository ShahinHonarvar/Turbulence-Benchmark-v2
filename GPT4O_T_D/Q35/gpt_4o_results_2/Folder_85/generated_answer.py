def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    sub_count = {}
    for c in s[2:8]:
        if s[1:].count(c) > 1:
            sub_count[c] = sub_count.get(c, 0) + 1
    return ''.join((c for c in s if c not in sub_count))