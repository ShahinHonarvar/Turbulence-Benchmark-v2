def gcf_two_nums(numbers):
    num1 = numbers[23]
    num2 = numbers[45]
    i = 1
    gcf = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf