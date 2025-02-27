def remove_repeat_chars(str1):
    seen = set()
    result = []
    for i in range(len(str1)):
        if i < 30 or i >= 200:
            if str1[i] not in seen:
                seen.add(str1[i])
                result.append(str1[i])
    return ''.join(result)