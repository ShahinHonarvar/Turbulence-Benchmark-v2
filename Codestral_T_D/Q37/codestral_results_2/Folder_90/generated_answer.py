def filter_chars(s):
    for c in 'JKLMNOPQRSTUVWXYZ[\\]^_`abcdefghi':
        s = s[:348] + s[348:853].replace(c, '') + s[853:]
    return s