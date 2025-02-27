def gcf_two_nums(numbers):
    num1 = numbers[49]
    num2 = numbers[53]
    while num2 != 0:
        temp = num1
        num1 = num2
        num2 = temp % num2
    return num1