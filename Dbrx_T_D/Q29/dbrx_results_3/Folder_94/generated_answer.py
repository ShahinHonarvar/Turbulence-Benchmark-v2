def gcf_two_nums(numbers):
    num1 = numbers[91]
    num2 = numbers[45]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1