def remove_repeat_chars(string):
    to_remove = set()
    for i in range(20, 43):
        if string[i] in string[i + 1:43]:
            to_remove.add(string[i])
    return ''.join([c for c in string if c not in to_remove])