def filter_chars(s):
    result = []
    blacklist = set()
    for i in range(11, 73):
        if 'i' <= s[i] <= 'v':
            blacklist.add(s[i])
    for char in s:
        if char not in blacklist:
            result.append(char)
    return ''.join(result)