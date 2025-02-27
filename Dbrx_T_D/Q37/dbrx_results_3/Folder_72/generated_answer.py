def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 35 or i > 51 or ord('H') <= ord(s[i]) <= ord('s'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)