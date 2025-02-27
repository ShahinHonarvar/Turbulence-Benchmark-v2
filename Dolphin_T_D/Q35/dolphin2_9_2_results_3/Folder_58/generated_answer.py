def remove_repeat_chars(string):
    remove_set = set()
    for i in range(103, 802):
        if string.count(string[i]) > 1:
            remove_set.add(string[i])
    new_string = ''.join([char for char in string if char not in remove_set])
    return new_string