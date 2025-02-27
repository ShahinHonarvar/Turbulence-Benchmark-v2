def remove_repeat_chars(str):
    result = []
    for ind, i in enumerate(str[1:4]):
        if result and i == result[-1]:
            continue
        result.append(i)
    return ''.join(result)