def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if 22 <= i <= 85:
            if '7' <= string[i] <= 'e':
                continue
        result += string[i]
    return result