def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 20 <= i <= 62 and 'i' <= s[i] <= 'k':
            result += ''.join((char for char in s if char != s[i]))
        else:
            result = s
    return result if result else s