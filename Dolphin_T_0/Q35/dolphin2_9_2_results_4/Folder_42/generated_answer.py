def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(18, 60):
        if s[i] in s[i + 1:60]:
            repeat_chars.add(s[i])
    return ''.join([c for c in s if c not in repeat_chars])