def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 114 <= i <= 639 and '!' <= char <= 'x':
            result.append(char)
    final_result = []
    for char in s:
        if char not in result:
            final_result.append(char)
    return ''.join(final_result)