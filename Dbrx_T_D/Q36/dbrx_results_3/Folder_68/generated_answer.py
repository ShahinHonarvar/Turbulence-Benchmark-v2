def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(1, min(9, len(s))):
        char = s[i]
        if '8' < char < 'm':
            filtered_chars.append(char)
    return ''.join((c for c in s if c not in filtered_chars))