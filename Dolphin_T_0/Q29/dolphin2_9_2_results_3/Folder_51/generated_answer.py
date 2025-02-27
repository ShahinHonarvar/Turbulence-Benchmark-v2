def gcf_two_nums(numbers):
    num1 = numbers[46]
    num2 = numbers[84]
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(small, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1