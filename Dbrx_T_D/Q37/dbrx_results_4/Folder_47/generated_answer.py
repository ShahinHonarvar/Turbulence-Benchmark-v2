def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if i < 38 or i > 54 or ord(s[i]) < ord(':') or (ord(s[i]) > ord('r')):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)