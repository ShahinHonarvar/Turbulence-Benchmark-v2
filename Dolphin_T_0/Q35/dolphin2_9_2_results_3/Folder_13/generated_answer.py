def remove_repeat_chars(s):
    result_str = ''
    for i in range(46, 91):
        if s[i] not in result_str:
            result_str += s[i]
    return result_str