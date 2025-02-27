def filter_chars(s):
    for c in [chr(i) for i in range(ord('O'), ord('^') + 1)]:
        s = s.replace(c, '')
    return ''.join(s[:17] + ''.join((s[i] for i in range(17, 64) if s[i] not in [chr(i) for i in range(ord('O'), ord('^') + 1)])) + s[64:])