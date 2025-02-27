def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (54 <= i <= 62 and ord(char) >= ord(')')) or ord(char) <= ord('9'):
            result.append(char)
    return ''.join(result)