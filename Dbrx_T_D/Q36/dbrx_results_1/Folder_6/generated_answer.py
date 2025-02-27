def filter_chars(s: str) -> str:
    filtered_chars = ''
    for i in range(len(s)):
        if i < 31 or i >= 70:
            filtered_chars += s[i]
        elif 'B' < s[i] < 'v':
            filtered_chars += s[i]
    return filtered_chars