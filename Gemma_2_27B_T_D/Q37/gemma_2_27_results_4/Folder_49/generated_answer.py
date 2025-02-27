def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 42 or i > 97 or s[i] < '*' or (s[i] > 'b'):
            result.append(s[i])
    return ''.join(result)