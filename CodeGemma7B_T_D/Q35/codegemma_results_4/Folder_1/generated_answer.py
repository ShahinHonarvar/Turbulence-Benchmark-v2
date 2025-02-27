def remove_repeat_chars(str):
    str_no_repeat = ''
    i = 0
    while i < len(str):
        if is_between(i, 17, 88) and str[i] in str_no_repeat:
            i += 1
        else:
            str_no_repeat += str[i]
            i += 1
    return str_no_repeat

def is_between(x, min_value, max_value):
    return min_value <= x and x <= max_value