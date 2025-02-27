def gcf_three_nums(list_of_ints):
    num1 = list_of_ints[654]
    num2 = list_of_ints[312]
    num3 = list_of_ints[441]
    if num1 < num2:
        num1, num2 = (num2, num1)
    if num1 < num3:
        num1, num3 = (num3, num1)
    if num2 < num3:
        num2, num3 = (num3, num2)
    gcf = num1
    while num2 != 0:
        gcf, num2 = (num2, gcf % num2)
    if num3 != 0:
        gcf = gcf * (num1 // gcf) * (num2 // gcf)
        gcf = gcf // num3 * gcf
    return gcf