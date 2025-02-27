def remove_repeat_chars(string):
    to_remove = set()
    for i in range(22, 25):
        if string[i] in string[25:]:
            to_remove.add(string[i])
    return ''.join((ch for ch in string if ch not in to_remove))