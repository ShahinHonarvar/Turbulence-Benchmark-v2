def gcf_two_nums(list_num):
    num1 = list_num[300]
    num2 = list_num[616]
    low_num = min(num1, num2)
    gcf = 0
    for i in range(1, low_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf