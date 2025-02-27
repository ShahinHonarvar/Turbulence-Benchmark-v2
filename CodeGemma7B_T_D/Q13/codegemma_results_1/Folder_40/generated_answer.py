def find_second_largest_num(num):
    num.sort()
    if len(num) < 2:
        return 'None'
    return num[-2]