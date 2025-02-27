def filter_chars(s):
    result = list(s)
    for i in range(20, 80):
        if i < len(result) and ord(result[i]) >= ord('!') and (ord(result[i]) <= ord('T')):
            char = result[i]
            while char in result:
                result.remove(char)
    return ''.join(result)