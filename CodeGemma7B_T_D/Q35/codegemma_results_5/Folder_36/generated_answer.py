def remove_repeat_chars(str):
    s = str[:476] + ''.join([c for c in str[476:709] if c not in str[476:709][i + 1:] and str.index(c) > i for i, c in enumerate(str[476:709])]) + str[709:]
    return s