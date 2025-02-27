def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, len(s) if len(s) < 7 else 7):
        if s[i] in s[1:i] + s[i + 1:7]:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))