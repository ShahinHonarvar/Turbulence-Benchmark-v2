def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    middle_chars = s[1:7]
    repeat_chars = {c for c in middle_chars if middle_chars.count(c) > 1}
    result = s[0] + ''.join((c for c in s[1:-1] if c not in repeat_chars)) + s[-1]
    return result