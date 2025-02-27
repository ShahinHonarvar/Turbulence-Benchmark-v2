def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if not (38 <= i <= 69 and s[i] >= 'H' and (s[i] <= 'e')):
            result += s[i]
    return result