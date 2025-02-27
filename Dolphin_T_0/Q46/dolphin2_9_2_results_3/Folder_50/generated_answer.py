def gcf_three_nums(numbers):
    num1 = numbers[20]
    num2 = numbers[35]
    num3 = numbers[74]
    i = 1
    while i <= num1:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factor = i
        i += 1
    return factor