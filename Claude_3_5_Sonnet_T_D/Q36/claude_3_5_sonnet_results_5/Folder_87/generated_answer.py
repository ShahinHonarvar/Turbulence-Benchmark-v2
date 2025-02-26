def filter_chars(s):
    result = []
    for char in s:
        if ord(char) <= 32 or ord(char) >= 61 or (not '3' < char < 'D'):
            result.append(char)
    return ''.join(result)