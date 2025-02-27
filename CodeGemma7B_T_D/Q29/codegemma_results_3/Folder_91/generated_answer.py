def gcf_two_nums(num_list):
    num1 = num_list[4]
    num2 = num_list[0]
    greater = max(num1, num2)
    smaller = min(num1, num2)
    gcf = 1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf