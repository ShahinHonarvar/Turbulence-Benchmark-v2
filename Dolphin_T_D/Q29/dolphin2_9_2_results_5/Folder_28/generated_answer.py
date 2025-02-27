def gcf_two_nums(data):
    num1 = data[48]
    num2 = data[76]
    if num1 > num2:
        n1 = num1
        n2 = num2
    else:
        n1 = num2
        n2 = num1
    while n2 != 0:
        n1 = n1 % n2
        n2 = n1 - n2
    return n1