def filter_chars(s):

    def should_remove(c):
        return ord('(') < ord(c) < ord('W')
    chars_to_remove = set((s[i] for i in range(57, 69) if should_remove(s[i])))
    return ''.join((c for c in s if c not in chars_to_remove))