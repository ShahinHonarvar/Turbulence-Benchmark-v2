def remove_repeat_chars(str):
    str = str[:43] + ''.join([char for char, counts in Counter(str[43:70]).items() for _ in range(counts)]) + str[70:]
    return str