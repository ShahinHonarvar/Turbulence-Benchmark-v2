def gcf_two_nums(numbers_list):
    num1 = numbers_list[380]
    num2 = numbers_list[327]
    gcf = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf