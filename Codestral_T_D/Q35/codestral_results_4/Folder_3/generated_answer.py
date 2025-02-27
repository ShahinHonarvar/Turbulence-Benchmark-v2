def remove_repeat_chars(s):
    to_remove = set()
    for char in s[56:88]:
        if s.count(char) > 1:
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))