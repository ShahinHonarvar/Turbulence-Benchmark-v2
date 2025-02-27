def filter_chars(s):
    for c in range(ord('!'), ord('}')):
        if any((s[i] == chr(c) for i in range(170, 195))):
            s = ''.join((c for c in s if c != chr(c)))
    return s