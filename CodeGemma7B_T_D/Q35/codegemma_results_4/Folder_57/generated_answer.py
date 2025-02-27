def remove_repeat_chars(arg):
    temp = arg[:25] + ''.join([k for i, k in enumerate(arg[25:80], start=25) if i + 1 >= k.count(k)]) + arg[80:]
    return temp