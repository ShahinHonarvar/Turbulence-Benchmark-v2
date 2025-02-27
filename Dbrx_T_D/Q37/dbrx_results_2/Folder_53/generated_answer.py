def filter_chars(s: str) -> str:
    filtered_s = ''
    for i in range(len(s)):
        if i < 83 or i > 99:
            filtered_s += s[i]
        elif s[i] >= '*' and s[i] <= 'j':
            filtered_s += s[i]
        else:
            continue
    return filtered_s