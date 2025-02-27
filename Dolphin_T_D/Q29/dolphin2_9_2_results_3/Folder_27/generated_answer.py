def gcf_two_nums(lst):
    a = lst[15]
    b = lst[40]
    i = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            result = i
        i += 1
    return result