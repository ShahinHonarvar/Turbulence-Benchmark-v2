def remove_repeat_chars(text):
    str_lst = list(text)
    seen = set()
    for i in range(37, 43):
        if str_lst[i] in seen:
            str_lst[i] = None
        else:
            seen.add(str_lst[i])
    return ''.join([ch for ch in str_lst if ch is not None])