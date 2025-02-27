def gcf_two_nums(numbers):
    num_1 = numbers[28]
    num_2 = numbers[49]
    divisor = min(num_1, num_2)
    while divisor > 1:
        if num_1 % divisor == 0 and num_2 % divisor == 0:
            break
        divisor -= 1
    return divisor