def gcf_two_nums(numbers):
    num1 = numbers[29]
    num2 = numbers[74]
    gcd_value = num2
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num2