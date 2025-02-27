def remove_repeat_chars(str1):
    seen = set()
    seen.add(str1[0])
    result = ''
    for i in range(1, len(str1) - 1):
        if str1[i] not in seen or i < 7:
            result += str1[i]
            seen.add(str1[i])
    return result + str1[-1]