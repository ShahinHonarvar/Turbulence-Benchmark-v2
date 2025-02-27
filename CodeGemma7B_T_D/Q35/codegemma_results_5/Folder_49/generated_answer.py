def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 90 or i > 200 or string[:i].count(c) <= 1])