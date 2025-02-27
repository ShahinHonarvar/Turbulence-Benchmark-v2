def gcf_two_nums(int_list):
    num1 = int_list[224]
    num2 = int_list[663]
    i = 1
    gcf = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf