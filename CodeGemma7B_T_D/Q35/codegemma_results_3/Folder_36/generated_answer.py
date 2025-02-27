def remove_repeat_chars(n):
    return ''.join(sorted(list(n), key=n.index))