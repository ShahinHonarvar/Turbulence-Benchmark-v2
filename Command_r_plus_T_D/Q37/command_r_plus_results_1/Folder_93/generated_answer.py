def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(38, 70):
        if 'H' <= s[i] <= 'e':
            chars_to_remove.append(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))