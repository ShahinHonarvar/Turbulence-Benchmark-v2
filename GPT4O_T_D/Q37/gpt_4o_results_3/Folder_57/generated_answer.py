def filter_chars(s):
    remove_chars = set(s[27:86]).intersection(set('!"#$%&\'()*+,-./:;<=>?@AB'))
    return ''.join((c for c in s if c not in remove_chars))