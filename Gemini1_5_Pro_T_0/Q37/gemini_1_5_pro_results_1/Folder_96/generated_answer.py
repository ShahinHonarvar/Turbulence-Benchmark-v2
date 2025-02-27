def filter_chars(text):
    filtered_chars = text[86:93]
    result = []
    for char in text:
        if char in filtered_chars and '!' <= char <= 's':
            continue
        result.append(char)
    return ''.join(result)