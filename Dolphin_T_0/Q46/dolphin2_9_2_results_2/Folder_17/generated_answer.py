def gcf_three_nums(int_list):
    num1 = int_list[20]
    num2 = int_list[51]
    num3 = int_list[62]
    gcf = 1
    for i in range(2, min(num1, num2, num3) + 1):
        while num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf *= i
            num1 //= i
            num2 //= i
            num3 //= i
    return gcf