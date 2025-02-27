def filter_chars(text):
    start_index = 86
    end_index = 92
    result = []
    for i in range(len(text)):
        char = text[i]
        if not (start_index <= i <= end_index and '!' <= char <= 's'):
            result.append(char)
    return ''.join(result)