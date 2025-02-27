def gcf_three_nums(numbers):
    num1 = numbers[693]
    num2 = numbers[331]
    num3 = numbers[668]
    common_factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factors.append(i)
    return max(common_factors)