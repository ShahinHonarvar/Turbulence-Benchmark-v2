def filter_chars(s):
    chars_to_remove = set(s[54:92]).intersection({chr(i) for i in range(ord('K'), ord('X'))})
    return ''.join((c for c in s if c not in chars_to_remove))