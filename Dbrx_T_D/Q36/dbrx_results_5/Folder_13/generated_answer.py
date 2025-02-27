def filter_chars(s):
    start_idx = 322
    end_idx = 525
    chars_to_remove = []
    for i in range(start_idx, end_idx):
        if s[i] > ')' and s[i] < 'O':
            chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s