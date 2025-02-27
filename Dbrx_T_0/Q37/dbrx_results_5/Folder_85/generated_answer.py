def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 28 or i > 65 or (s[i] < 'O' or s[i] > 'd'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)