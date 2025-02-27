def remove_repeat_chars(str_param):
    mini = 50
    maxi = 74
    seen = set()
    result = []
    for char in str_param:
        if mini <= len(result) <= maxi and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)