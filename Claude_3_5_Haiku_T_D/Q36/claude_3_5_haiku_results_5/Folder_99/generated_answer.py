def filter_chars(s):
    if len(s) <= 948:
        return s
    filtered_chars = []
    for i, char in enumerate(s):
        if 476 < i < 948 and 'b' < char < 'd':
            filtered_chars.append(char)
    result = list(s)
    for char in filtered_chars:
        while char in result:
            result.remove(char)
    return ''.join(result)