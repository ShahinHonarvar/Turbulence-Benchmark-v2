def filter_chars(s):
    return ''.join((c for c in s if (ord(c) > ord('!') and ord(c) < ord('s')) and c not in set(s[81:86])))