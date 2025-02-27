def gcf_three_nums(num_list):
    num1 = num_list[56]
    num2 = num_list[54]
    num3 = num_list[13]
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num3 == 0:
        return num1
    i = min(num1, num2, num3)
    while i > 1:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
        i -= 1
    return 1