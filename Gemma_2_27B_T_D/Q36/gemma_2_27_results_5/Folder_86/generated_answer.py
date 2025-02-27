def filter_chars(text):
    result = list(text)
    for i in range(672, 709):
        char = text[i]
        if char > 'X' and char < '}':
            while char in result:
                result.remove(char)
    return ''.join(result)