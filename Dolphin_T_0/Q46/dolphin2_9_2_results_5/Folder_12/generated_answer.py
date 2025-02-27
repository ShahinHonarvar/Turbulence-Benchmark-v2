def gcf_three_nums(numbers):
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]
    gcf = min(num1, num2, num3)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        else:
            gcf -= 1
    return 1