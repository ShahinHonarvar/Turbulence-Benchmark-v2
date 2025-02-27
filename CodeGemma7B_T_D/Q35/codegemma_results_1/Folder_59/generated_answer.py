def remove_repeat_chars(str):
    seen = set()
    for i in range(len(str)):
        if i >= 0 and i <= 10 and (str[i] in seen):
            str = str[:i] + str[i + 1:]
        else:
            seen.add(str[i])
    return str