def remove_repeat_chars(str1):
    return ''.join([x for x in str1 if x not in str1[2:5] or x not in str1[str1.index(x):]])