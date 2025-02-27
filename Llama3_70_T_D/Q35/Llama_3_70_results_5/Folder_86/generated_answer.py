def remove_repeat_chars(s):
    seen = set()
    repeat_chars = set()
    for i in range(19, 32):
        if s[i] in seen:
            repeat_chars.add(s[i])
        seen.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))