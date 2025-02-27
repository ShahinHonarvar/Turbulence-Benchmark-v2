def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    middle_chars = s[42:87]
    repeat_chars = {c for c in middle_chars if middle_chars.count(c) > 1}
    result = ''.join((c for c in s if c not in repeat_chars))
    return result