def filter_chars(s):
    to_be_removed = ''.join([ch for i, ch in enumerate(s[219:403]) if '*' < ch < '7'])
    return ''.join([ch for ch in s if ch not in to_be_removed])