def gcf_two_nums(lst):
    num1 = lst[90]
    num2 = lst[41]
    greater = max(num1, num2)
    lesser = min(num1, num2)
    while lesser != 0:
        greater, lesser = (lesser, greater % lesser)
    return greater