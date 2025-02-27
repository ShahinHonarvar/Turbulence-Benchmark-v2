def filter_chars(text):
    result = []
    for i in range(66, 90):
        if ord(text[i]) > ord('#') and ord(text[i]) < ord('T'):
            result.append(text[i])
    return ''.join(result)