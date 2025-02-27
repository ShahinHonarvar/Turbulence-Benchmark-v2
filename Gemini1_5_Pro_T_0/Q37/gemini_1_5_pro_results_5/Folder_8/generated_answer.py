def filter_chars(text):
    start_index = 41
    end_index = 86
    result = []
    for i, char in enumerate(text):
        if i in range(start_index, end_index + 1) and 'S' <= char <= 's':
            if char not in result:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)