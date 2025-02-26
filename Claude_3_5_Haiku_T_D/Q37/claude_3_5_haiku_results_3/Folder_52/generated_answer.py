def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 54 <= i <= 83 and 'j' <= s[i] <= 'v':
            result += ''.join((char for char in s if char != s[i]))
        else:
            result += s[i]
    return result