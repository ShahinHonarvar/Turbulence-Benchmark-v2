def gcf_two_nums(numbers):
    num1 = numbers[88]
    num2 = numbers[35]
    divisor = max(num1, num2)
    while divisor > 1:
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
        else:
            divisor -= 1
    return 1