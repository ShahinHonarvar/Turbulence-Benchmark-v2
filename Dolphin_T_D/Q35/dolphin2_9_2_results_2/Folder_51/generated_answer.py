def remove_repeat_chars(s):
    to_remove = set()
    for i in range(7, 10):
        if s[i] in s[10:]:
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))