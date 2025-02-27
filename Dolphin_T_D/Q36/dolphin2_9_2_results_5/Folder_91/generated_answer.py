def filter_chars(s):
    remove = [s[i] for i in range(1, 3) if ord(s[i]) > ord('$') and ord(s[i]) < ord('?')]
    for r in remove:
        s = s.replace(r, '')
    return s