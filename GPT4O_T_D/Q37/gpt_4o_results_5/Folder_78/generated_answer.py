def filter_chars(s):
    to_remove = set(s[75:100]).intersection(set('89:;<=>?@ABCDEabcde'))
    return ''.join((c for c in s if c not in to_remove))