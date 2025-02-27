def filter_chars(s):
    return ''.join((c for c in s if c not in set(s[35:52]) or not s[35:52] <= c <= 's'))

def main(s, c):
    return filter_chars(s.translate({ord(c): None for c in s[35:52]}))