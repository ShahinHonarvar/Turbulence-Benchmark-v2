def gcf_two_nums(numbers):
    num1 = numbers[54]
    num2 = numbers[13]
    divisor = min(num1, num2)
    while divisor > 1:
        if num1 % divisor != 0 or num2 % divisor != 0:
            divisor -= 1
        else:
            return divisor
    return 1