def filter_chars(s):
    chars_to_remove = set(s[31:50]).intersection({chr(i) for i in range(ord('/'), ord('J'))})
    return ''.join((c for c in s if c not in chars_to_remove))