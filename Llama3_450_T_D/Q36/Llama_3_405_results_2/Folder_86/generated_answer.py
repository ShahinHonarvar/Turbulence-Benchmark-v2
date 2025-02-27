def filter_chars(s):
    chars_to_remove = set()
    for i in range(672, 709):
        if 672 <= i < len(s) < 709:
            char = s[i]
            if 'X' < char < '}':
                chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))