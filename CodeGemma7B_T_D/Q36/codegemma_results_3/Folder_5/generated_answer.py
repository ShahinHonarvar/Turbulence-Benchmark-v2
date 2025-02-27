def filter_chars(s):
    result = s
    for letter in range(55, 66):
        if ord(result[letter]) > ord('f') and ord(result[letter]) < ord('|'):
            result = result.replace(a, '')
    return result