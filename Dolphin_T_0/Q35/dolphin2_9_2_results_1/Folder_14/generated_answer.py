def remove_repeat_chars(string):
    to_remove = {}
    for i in range(2, 6):
        if string[i] in to_remove:
            to_remove[string[i]] += 1
        else:
            to_remove[string[i]] = 1
    result = [x for x in string if x not in to_remove or to_remove[x] == 1]
    return ''.join(result)