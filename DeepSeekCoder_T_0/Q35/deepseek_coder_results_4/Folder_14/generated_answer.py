def remove_repeat_chars(s):
    to_remove = set()
    for i in range(2, len(s) if len(s) < 5 else 5):
        if s[i] in s[2:i] or s[i] in s[i + 1:5]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result