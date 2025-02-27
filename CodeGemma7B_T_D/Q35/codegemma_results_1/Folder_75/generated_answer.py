def remove_repeat_chars(str1):
    new_str = str1[0:20]
    seen = set()
    for i in reversed(range(20, 51)):
        if str1[i] not in seen:
            seen.add(str1[i])
            new_str += str1[i]
    return new_str[::-1]