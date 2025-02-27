def gcf_two_nums(numbers):
    num1 = numbers[28]
    num2 = numbers[49]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1