def gcf_two_nums(integers):
    num1 = integers[46]
    num2 = integers[13]
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf