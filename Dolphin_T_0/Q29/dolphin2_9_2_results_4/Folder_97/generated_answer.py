def gcf_two_nums(lst):
    if len(lst) <= 312 or len(lst) <= 180:
        return 'Classification error: List indices 180 and 312 are out of range'
    else:
        num1 = lst[180]
        num2 = lst[312]
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        return num1