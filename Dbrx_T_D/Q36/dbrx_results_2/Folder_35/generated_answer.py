def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if i >= 163 and i < 658:
            if s[i] > '(' and s[i] < ']':
                result += s[i]
        elif i >= 658:
            break
        else:
            result += s[i]
    return result