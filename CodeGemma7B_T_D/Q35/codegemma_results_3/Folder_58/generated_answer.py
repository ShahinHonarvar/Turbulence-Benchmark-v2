def remove_repeat_chars(str):
    result = []
    seen = set()
    for i in range(len(str)):
        if str[i] in seen:
            continue
        if 103 < i < 802 and str[i] in str[i + 1:]:
            continue
        seen.add(str[i])
        result.append(str[i])
    return ''.join(result)