def filter_chars(txt):

    def keep(c):
        return ord('f') > c > ord('5') and c not in txt[51:76] and (51 <= txt.index(c) < 76)
    return ''.join((c for c in txt if keep(c)))