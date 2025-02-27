def remove_repeat_chars(str1):
    new_str = str1[:476] + ''.join([ch for i, ch in enumerate(str1[476:709]) if i == str1[476:709].index(ch)]) + str1[709:]
    return new_str