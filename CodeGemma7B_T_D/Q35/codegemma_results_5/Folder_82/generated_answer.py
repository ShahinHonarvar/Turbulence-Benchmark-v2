def remove_repeat_chars(given_str):
    seen = set()
    result = []
    for i in range(200, 30, -1):
        if given_str[i] not in seen and given_str[i] not in result:
            result.append(given_str[i])
    for i in range(30, 0, -1):
        if given_str[i] not in seen:
            result.append(given_str[i])
    return ''.join(result[::-1])