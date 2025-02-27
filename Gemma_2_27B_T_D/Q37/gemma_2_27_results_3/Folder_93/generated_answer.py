def filter_chars(s):
    result = []
    for i in range(len(s)):
        if not (38 <= i <= 69 and 'H' <= s[i] <= 'e'):
            result.append(s[i])
    return ''.join(result)