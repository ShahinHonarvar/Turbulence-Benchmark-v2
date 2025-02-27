def custom_sort_key(a, b):
    if len(str(a)) == len(str(b)):
        return 0
    elif len(str(a)) < len(str(b)):
        return -1
    else:
        return 1