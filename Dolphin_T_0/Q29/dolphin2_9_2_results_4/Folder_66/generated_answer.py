def gcf_two_nums(list_of_ints):
    num1 = list_of_ints[86]
    num2 = list_of_ints[89]
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    while num1 != num2:
        if num1 < num2:
            num2 = num2 - num1
        else:
            num1 = num1 - num2
    return num1