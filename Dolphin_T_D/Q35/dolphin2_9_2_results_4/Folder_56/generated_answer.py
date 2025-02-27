def remove_repeat_chars(s):
    chars_to_remove = [c for c, _ in collections.Counter(s[7:10]).items() if _ > 1]
    return ''.join([c for c in s if c not in chars_to_remove])