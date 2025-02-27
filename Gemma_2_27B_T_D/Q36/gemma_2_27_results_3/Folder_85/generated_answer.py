def filter_chars(text):
    result = list(text)
    for i in range(55, 80):
        if chr(i) > 'S' and chr(i) < 's':
            while chr(i) in result:
                result.remove(chr(i))
    return ''.join(result)