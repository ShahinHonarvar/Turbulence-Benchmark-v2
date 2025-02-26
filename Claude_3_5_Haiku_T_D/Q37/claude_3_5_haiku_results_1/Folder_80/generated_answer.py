def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 36 <= i <= 79 and 'a' <= s[i] <= 'i':
            result += ''.join((char for char in s if char != s[i]))
        elif result:
            result += s[i]
        else:
            result += s[i]
    return result