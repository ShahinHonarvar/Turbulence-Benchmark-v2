from functools import cmp_to_key

def return_n_greatest_chars(str):

    def compare(x, y):
        if ord(x) < ord(y):
            return 1
        elif ord(x) > ord(y):
            return -1
        else:
            return 0
    list = sorted(list(str), key=cmp_to_key(compare), reverse=True)
    if len(list) <= 31:
        return list
    else:
        return list[:31]