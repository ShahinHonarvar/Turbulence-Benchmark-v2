def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    sub_str = s[33:99]
    char_count = {c: sub_str.count(c) for c in set(sub_str)}
    to_remove = {c for c in char_count if char_count[c] > 1}
    return ''.join((c for c in s if c not in to_remove))