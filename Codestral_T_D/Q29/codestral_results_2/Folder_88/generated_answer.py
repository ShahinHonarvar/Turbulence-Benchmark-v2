def gcf_two_nums(numbers):
    num1 = numbers[27]
    num2 = numbers[34]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1