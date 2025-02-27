def filter_chars(s):
    chars_to_remove = set(s[722:833]) & set('KLMNlmnopqrstuvwxyzabcdefghijklm')
    return ''.join((c for c in s if c not in chars_to_remove))