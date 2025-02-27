def return_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    chars = s[69:82]
    res = []
    for c in chars:
        if c in v and ord(' ') < ord(c) <= ord('~'):
            res.append(c)
    return res