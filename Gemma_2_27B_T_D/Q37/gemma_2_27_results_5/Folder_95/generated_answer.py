def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (35 <= i <= 40 and ord(')') <= ord(char) <= ord('l')):
            result.append(char)
    return ''.join(result)