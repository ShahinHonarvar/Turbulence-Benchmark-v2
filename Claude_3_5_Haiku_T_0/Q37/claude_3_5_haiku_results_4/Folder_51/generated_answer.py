def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 36 <= i <= 40 and 'H' <= char <= 'e':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string