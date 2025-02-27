def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('!') + 1, ord('A'))))
    s = list(s)
    for i in range(11, 46):
        if i >= len(s):
            break
        if s[i] in to_remove:
            s = [c for c in s if c != s[i]]
    return ''.join(s)