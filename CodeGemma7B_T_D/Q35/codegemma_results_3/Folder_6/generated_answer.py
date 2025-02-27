def remove_repeat_chars(txt):
    result = []
    for i in range(len(txt)):
        if i >= 20 and i <= 93:
            if txt[i] not in result:
                result.append(txt[i])
    return ''.join(result)