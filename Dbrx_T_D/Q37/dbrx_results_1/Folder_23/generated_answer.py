def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 51 or i > 77 or (i >= 51 and i <= 77 and (ord(s[i]) < 86 or ord(s[i]) > 89)):
            result += s[i]
    return result