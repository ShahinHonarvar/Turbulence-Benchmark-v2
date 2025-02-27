def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 10 or i > 69 or (s[i] < 'I' or s[i] > 'K'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)