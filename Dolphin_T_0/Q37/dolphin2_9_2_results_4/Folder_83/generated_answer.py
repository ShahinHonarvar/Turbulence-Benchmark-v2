def filter_chars(s):
    for ch in range(ord('K'), ord('z') + 1):
        s = s[:29] + ''.join((c for c in s[29:80] if c != chr(ch))) + s[80:]
    return s