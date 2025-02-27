def remove_repeat_chars(s):
    repeat_chars = {s[i] for i in range(1, 4) if s[i] in s[1:i] or s[i] in s[i + 1:4]}
    return ''.join((c for c in s if c not in repeat_chars))