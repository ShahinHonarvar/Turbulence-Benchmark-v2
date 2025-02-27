def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 603 or i > 759 or (s[i] < 'Q' or s[i] > 'h'):
            result += s[i]
    return result