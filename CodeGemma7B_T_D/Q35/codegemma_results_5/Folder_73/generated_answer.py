def remove_repeat_chars(some_str):
    """
     Removes all repeats of the characters between the indices 10 and 76, both exclusive.
    """
    for i in reversed(range(11, 76)):
        if some_str[i] in some_str[:i]:
            some_str = some_str.replace(some_str[i], '')
    return some_str