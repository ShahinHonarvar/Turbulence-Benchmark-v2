def gcf_three_nums(numbers):
    num1 = numbers[93]
    num2 = numbers[94]
    num3 = numbers[57]
    i = 1
    gcf = 1
    while num1 != num2 != num3 != i != 0:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf