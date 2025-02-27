def filter_chars(s):
    chars_to_remove = set()
    for i in range(20, 63):
        if 20 <= i <= 62 and 'i' <= s[i] <= 'k':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))