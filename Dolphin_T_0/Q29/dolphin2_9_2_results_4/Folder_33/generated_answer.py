def gcf_two_nums(numbers):
    if numbers is None:
        return 0
    num1 = numbers[166]
    num2 = numbers[106]
    gcf = min(num1, num2)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0:
            return gcf
        gcf -= 1
    return 1