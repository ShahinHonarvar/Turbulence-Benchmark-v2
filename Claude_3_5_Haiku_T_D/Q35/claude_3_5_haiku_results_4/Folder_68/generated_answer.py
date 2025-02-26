def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    to_remove = set()
    for char in s[:10]:
        if s[:10].count(char) > 1 and char not in to_remove:
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))