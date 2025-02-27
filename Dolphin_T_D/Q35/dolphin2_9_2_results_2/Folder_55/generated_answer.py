def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(10, 100):
        if s[i] in s[:10] or s[i] in s[100:]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))