def filter_chars(s):
    chars_to_remove = ['S', '[', '#', '$', '%', '&', '{', '}']
    for char in s[78:81]:
        if 'S' < char < '[':
            s = ''.join([c for c in s if c not in chars_to_remove])
    return s