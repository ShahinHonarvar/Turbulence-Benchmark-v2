def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(7, min(9, len(s)) + 1):
        if '6' <= s[i] <= 'w':
            chars_to_remove.append(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))