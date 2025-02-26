def filter_chars(s):
    result = list(s)
    for i in range(len(s)):
        if 48 < i < 75 and '6' < s[i] < '_':
            result = [char for char in result if char != s[i]]
    return ''.join(result)