def filter_chars(s):
    to_remove = [s[i] for i in range(58, 81) if '5' < s[i] < '>']
    for ch in set(to_remove):
        if ch in to_remove:
            s = s.replace(ch, '')
    return s