def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 11 or i > 72:
            filtered_chars.append(s[i])
        elif s[i] >= 'i' and s[i] <= 'v':
            continue
        else:
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)