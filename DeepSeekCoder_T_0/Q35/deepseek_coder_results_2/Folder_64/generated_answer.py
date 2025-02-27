def remove_repeat_chars(s):
    if len(s) <= 1:
        return s
    chars_to_remove = {s[i] for i in range(1, 5) if s[i] in s[1:i] + s[i + 1:5]}
    return ''.join((c for c in s if c not in chars_to_remove))