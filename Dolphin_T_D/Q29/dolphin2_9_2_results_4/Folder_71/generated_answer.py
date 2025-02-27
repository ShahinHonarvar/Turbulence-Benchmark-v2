def gcf_two_nums(num_list):
    num1 = num_list[78]
    num2 = num_list[93]
    i = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf