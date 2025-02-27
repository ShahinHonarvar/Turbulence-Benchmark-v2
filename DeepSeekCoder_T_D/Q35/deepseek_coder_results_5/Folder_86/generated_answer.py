def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(20, 32):
        if s[i] in s[20:32] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    result = ''.join((c for c in s if c not in repeat_chars))
    return result