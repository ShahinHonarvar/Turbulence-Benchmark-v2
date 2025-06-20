def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    sub_str = s[18:88]
    repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
    result = s[:18] + ''.join((c for c in s[18:88] if c not in repeat_chars)) + s[88:]
    return result