def filter_chars(s):
    for c in [chr(i) for i in range(ord('i'), ord('v') + 1)]:
        s = s[:11] + s[11:73].replace(c, '') + s[73:]
    return s