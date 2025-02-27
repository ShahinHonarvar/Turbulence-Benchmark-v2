def filter_chars(s):
    for char in sorted(set((s[i] for i in range(28, 66) if 'O' <= s[i] <= 'd'))):
        s = s.replace(char, '')
    return s