def filter_chars(s):
    b = s[323:526]
    b = ''.join([i for i in b if i > ')' and i < 'O'])
    return ''.join([i for i in s if i not in b])