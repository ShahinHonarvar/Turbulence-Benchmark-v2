def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 22 <= i <= 85 and '7' <= char <= 'e':
            result.append(char)
    filtered_str = s
    for char in result:
        filtered_str = filtered_str.replace(char, '')
    return filtered_str