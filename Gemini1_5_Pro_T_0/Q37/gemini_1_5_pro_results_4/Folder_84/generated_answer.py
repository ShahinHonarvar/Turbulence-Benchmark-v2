def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 138 and i <= 920 and (s[i] >= '6') and (s[i] <= 'A'):
            for char in s:
                if char != s[i]:
                    new_s += char
            s = new_s
            new_s = ''
        else:
            new_s += s[i]
    return new_s