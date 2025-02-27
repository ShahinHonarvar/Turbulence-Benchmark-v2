def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 22:
        for char in s[22:25]:
            if '5' < char < '}':
                chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))