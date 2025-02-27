def remove_repeat_chars(a):
    a = a[:86] + a[86:99].replace(a[86], '') + a[99:]
    return a