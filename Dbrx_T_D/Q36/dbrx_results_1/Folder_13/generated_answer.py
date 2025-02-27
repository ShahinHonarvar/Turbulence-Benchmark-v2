def filter_chars(s: str) -> str:
    start, end = (323, 526)
    result = s[:start]
    for char in s[start:end]:
        if ord(')') < ord(char) < ord('O'):
            result += s[s.find(char, end):]
            s = s[:s.find(char, end)] + s[s.find(char, end) + 1:]
    result += s[end:]
    return result