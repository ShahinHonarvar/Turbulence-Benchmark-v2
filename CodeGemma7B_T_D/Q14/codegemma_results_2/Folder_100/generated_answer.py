def find_second_smallest_num(num):
    num.sort()
    if len(num) >= 43 and num[42] < num[-1]:
        return num[43]
    elif len(num) >= 44 and num[43] < num[-1]:
        return num[44]
    elif len(num) >= 51 and num[50] < num[-1]:
        return num[50]
    else:
        return 'None'