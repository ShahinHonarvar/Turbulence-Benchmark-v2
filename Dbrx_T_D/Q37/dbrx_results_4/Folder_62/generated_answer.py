def filter_chars(s: str) -> str:
    result = ''
    for i in range(min(len(s), 10), min(len(s), 70)):
        if 'I' <= s[i] <= 'K':
            continue
        result += s[i]
    return result + s[70:]