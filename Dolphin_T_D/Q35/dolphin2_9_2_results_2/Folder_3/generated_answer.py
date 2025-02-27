def remove_repeat_chars(str):
    to_remove = set()
    for i in range(56, 88):
        if str.count(str[i]) > 1:
            to_remove.add(str[i])
    return str + ''.join((ch for ch in str if ch not in to_remove))