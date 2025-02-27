def remove_repeat_chars(a):
    return ''.join([c for c, i in zip(a, range(len(a))) if i < 20 or i > 43 or a.count(c, 20, 44) == 1])