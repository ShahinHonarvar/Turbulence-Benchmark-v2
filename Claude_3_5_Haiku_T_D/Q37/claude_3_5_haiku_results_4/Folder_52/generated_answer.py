def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 54 <= i <= 83 and 'j' <= char <= 'v':
            result += s[:i] + s[i + 1:]
        else:
            result += char
    return result