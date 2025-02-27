def filter_chars(s):
    to_remove = set()
    for char in s[114:640]:
        if '!' <= char <= 'x':
            to_remove.add(char)
    return ''.join([c for c in s if c not in to_remove])