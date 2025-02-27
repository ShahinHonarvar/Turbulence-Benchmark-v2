def gcf_two_nums(numbers):
    num1 = numbers[15]
    num2 = numbers[99]
    factor = 1
    while num1 >= factor and num2 >= factor:
        if num1 % factor == 0 and num2 % factor == 0:
            greatest_factor = factor
        factor += 1
    return greatest_factor