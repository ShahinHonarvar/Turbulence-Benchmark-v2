def remove_repeat_chars(s):
    seen = set()
    duplicates = set()
    for i in range(1, 4):
        if s[i] in seen:
            duplicates.add(s[i])
        else:
            seen.add(s[i])
    return ''.join((c for c in s if c not in duplicates))