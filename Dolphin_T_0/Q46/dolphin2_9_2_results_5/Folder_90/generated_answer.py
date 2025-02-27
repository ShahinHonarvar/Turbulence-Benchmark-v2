def gcf_three_nums(numbers):
    num1 = numbers[818]
    num2 = numbers[606]
    num3 = numbers[873]
    i = 1
    while i <= min(num1, num2, num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf