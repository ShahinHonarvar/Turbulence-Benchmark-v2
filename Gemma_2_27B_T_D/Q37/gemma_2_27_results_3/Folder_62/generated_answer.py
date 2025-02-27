def filter_chars(text):
    result = list(text)
    for i in range(10, 70):
        if i < len(text) and 'I' <= text[i] <= 'K':
            char = text[i]
            while char in result:
                result.remove(char)
    return ''.join(result)