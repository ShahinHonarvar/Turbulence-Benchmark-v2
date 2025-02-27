def remove_repeat_chars(str1):
    distinct_chars = []
    for i in range(len(str1)):
        if str1[i] not in distinct_chars:
            distinct_chars.append(str1[i])
    return ''.join(distinct_chars)