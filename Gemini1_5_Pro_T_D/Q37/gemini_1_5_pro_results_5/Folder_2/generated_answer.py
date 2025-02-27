def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 477 and i <= 984 and (s[i] >= ',') and (s[i] <= 'V'):
            for char in s:
                if char != s[i]:
                    new_s += char
            s = new_s
            new_s = ''
        else:
            new_s += s[i]
    return new_s