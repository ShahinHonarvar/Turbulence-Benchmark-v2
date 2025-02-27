def filter_chars(s):
    chars_to_remove = set(s[19:34]).intersection({chr(i) for i in range(ord('S'), ord('{') + 1)})
    return ''.join((c for c in s if c not in chars_to_remove))