def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 603 <= i <= 759 and 'Q' <= char <= 'h':
            result.append(char)
    filtered_string = ''.join(result)
    return s.replace(filtered_string, '')