def filter_chars(s: str) -> str:
    filtered_chars = ''
    for i in range(len(s)):
        if i > 0 and i < 9:
            if '8' < s[i] < 'm':
                continue
        filtered_chars += s[i]
    return filtered_chars