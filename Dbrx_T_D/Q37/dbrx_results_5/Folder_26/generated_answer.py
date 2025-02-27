def filter_chars(s: str) -> str:
    filtered_chars = ''
    for i in range(len(s)):
        if (i < 20 or i > 62) and s[i] >= 'i' and (s[i] <= 'k'):
            filtered_chars += s[i]
    return filtered_chars