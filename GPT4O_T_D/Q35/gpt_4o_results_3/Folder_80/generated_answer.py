def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(58, 84):
        if s[i] in s[58:84] and s[58:84].count(s[i]) > 1:
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove or not 57 < s.index(c) < 84))
    return result