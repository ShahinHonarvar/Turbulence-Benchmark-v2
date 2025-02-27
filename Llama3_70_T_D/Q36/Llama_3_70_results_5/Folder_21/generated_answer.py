def filter_chars(s):
    return s[:219] + ''.join((i for i in s[219:403] if not '*' < i < '7')) + s[403:]