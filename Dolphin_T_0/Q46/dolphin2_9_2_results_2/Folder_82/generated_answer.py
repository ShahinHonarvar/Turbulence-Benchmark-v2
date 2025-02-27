def gcf_three_nums(numbers):
    num1 = numbers[67]
    num2 = numbers[84]
    num3 = numbers[13]
    gcf = min(num1, num2, num3)
    while num1 % gcf != 0 or num2 % gcf != 0 or num3 % gcf != 0:
        gcf -= 1
    return gcf