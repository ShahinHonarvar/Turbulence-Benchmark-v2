def gcf_two_nums(numbers_list):
    num1 = numbers_list[300]
    num2 = numbers_list[616]
    gcf = 0
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf