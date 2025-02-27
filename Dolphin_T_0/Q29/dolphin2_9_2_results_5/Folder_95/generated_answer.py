def gcf_two_nums(numbers):
    num1 = numbers[43]
    num2 = numbers[99]
    i = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        else:
            gcf = 1
        i += 1
    return gcf