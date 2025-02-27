def filter_chars(s):
    if len(s) <= 476:
        return s
    subsequence = s[477:948]
    for char in subsequence:
        if 'b' < char < 'd':
            s = s.replace(char, '')
    return s