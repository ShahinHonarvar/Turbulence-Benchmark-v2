def gcf_three_nums(numbers):
    num1 = numbers[13]
    num2 = numbers[70]
    num3 = numbers[32]
    factors = []
    for i in range(1, max(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)