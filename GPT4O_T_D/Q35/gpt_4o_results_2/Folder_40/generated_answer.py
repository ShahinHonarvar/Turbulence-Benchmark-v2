def remove_repeat_chars(s):
    repeating_chars = set()
    for i in range(1, 3):
        if s[1:3].count(s[i]) > 1:
            repeating_chars.add(s[i])
    return ''.join((c for c in s if c not in repeating_chars))