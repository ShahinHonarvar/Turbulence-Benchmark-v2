def gcf_three_nums(numbers):
    num1 = numbers[27]
    num2 = numbers[85]
    num3 = numbers[51]
    for factor in range(1, min(num1, num2, num3) + 1):
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            gcf = factor
    return gcf