def remove_repeat_chars(k):
    p = k[89:91]
    for i in p:
        k = k.replace(i, '')
    return k