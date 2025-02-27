def remove_repeat_chars(s):
    to_remove = set()
    for i in range(48, 76):
        if s[i:].count(s[i]) > 1:
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))