def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 38 or i > 69 or s[i] < 'H' or (s[i] > 'e'):
            result.append(s[i])
    return ''.join(result)