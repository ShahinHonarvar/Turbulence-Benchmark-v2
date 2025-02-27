def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not 603 <= i <= 759 or not 'Q' <= s[i] <= 'h':
            result += s[i]
    return result