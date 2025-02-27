def filter_chars(text):
    result = []
    for i in range(18, 38):
        if text[i] > ')' and text[i] < 'P':
            for j in range(i, len(text)):
                if text[j] == text[i]:
                    text[j] = None
    for char in text:
        if char is not None:
            result.append(char)
    return ''.join(result)