def filter_chars(s):
    result = ''
    for char in s:
        if 155 <= s.index(char) <= 403:
            if '(' <= char <= ']':
                continue
        result += char
    return result