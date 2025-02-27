def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 15 or i > 55 or ord(s[i]) < ord('W') or (ord(s[i]) > ord('{')):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)