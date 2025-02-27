def filter_chars(s):
    charsToRemove = set()
    for i in range(31, len(s)):
        if 31 < i < 70 and 'B' < s[i] < 'v':
            charsToRemove.add(s[i])
    for char in charsToRemove:
        s = s.replace(char, '')
    return s