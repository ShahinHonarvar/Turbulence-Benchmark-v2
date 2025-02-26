def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 42 < i < 78 and '!' < char < '?':
            filtered_chars.append(char)
    result = list(s)
    for char in filtered_chars:
        while char in result:
            result.remove(char)
    return ''.join(result)