def gcf_two_nums(num_list):
    num1 = num_list[380]
    num2 = num_list[327]
    i = 1
    gcf = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf