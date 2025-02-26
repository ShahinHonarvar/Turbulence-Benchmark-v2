def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 170 < i < 195 and '!' < char < '}':
            filtered_chars.append(char)
    result = s
    for char in filtered_chars:
        result = result.replace(char, '')
    return result