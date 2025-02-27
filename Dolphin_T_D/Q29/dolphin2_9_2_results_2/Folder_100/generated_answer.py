def gcf_two_nums(numbers):
    num1 = numbers[96]
    num2 = numbers[32]
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1