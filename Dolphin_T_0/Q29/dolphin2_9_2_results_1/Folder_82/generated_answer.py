def gcf_two_nums(numbers):
    num1 = numbers[33]
    num2 = numbers[72]
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1