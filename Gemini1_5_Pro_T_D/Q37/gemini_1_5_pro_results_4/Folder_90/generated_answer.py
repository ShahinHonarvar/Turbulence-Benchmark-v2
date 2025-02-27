def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if not (348 <= i <= 852 and 'J' <= s[i] <= 'b'):
            new_s += s[i]
    return new_s