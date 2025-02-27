def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 38 or i > 99 or (s[i] < 'A' or s[i] > 'Q'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)