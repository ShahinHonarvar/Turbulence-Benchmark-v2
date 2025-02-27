def find_second_smallest_num(num):
    if not num:
        return None
    num.sort()
    if len(num) < 57:
        return None
    return num[56:67][1]