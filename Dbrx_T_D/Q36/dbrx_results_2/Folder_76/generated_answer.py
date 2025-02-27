def filter_chars(s):
    return ''.join((c for c in s[669:888] if c.lower() < 'b' or c.lower() > 'y')) + s[:669] + s[888:]