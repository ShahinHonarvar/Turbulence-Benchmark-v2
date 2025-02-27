def gcf_two_nums(numbers):
    num1 = numbers[198]
    num2 = numbers[212]
    if num1 % num2 == 0:
        return num2
    while num2 > 0:
        num1, num2 = (num2, num1 % num2)
    return num1