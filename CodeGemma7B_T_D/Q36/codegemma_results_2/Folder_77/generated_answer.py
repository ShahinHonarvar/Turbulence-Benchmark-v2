def filter_chars(s):
    for i in range(221, 419):
        if s[i] > '-' and s[i] < 'v':
            for j in range(len(s)):
                if s[j] == s[i]:
                    s[j] = ''
    return ''.join(s)