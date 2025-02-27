def filter_chars(s):
    indices_to_check = range(20, 69)
    chars_to_remove = set()
    for i in indices_to_check:
        if i < len(s) and '<' < s[i] < 'C':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))