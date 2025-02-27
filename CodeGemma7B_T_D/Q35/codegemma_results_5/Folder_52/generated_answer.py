def remove_repeat_chars(str):
    counter = {}
    new_str = ''
    for i in range(38, 81):
        if str[i] in counter:
            counter[str[i]] += 1
        else:
            counter[str[i]] = 1
    for i in range(len(str)):
        if counter[str[i]] > 1:
            continue
        new_str += str[i]
    return new_str