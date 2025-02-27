def remove_repeat_chars(s):
    if len(s) <= 52:
        return s
    subseq = s[39:52]
    duplicates = {c for c in subseq if subseq.count(c) > 1}
    return ''.join((c for c in s if c not in duplicates or s.index(c) not in range(40, 52)))