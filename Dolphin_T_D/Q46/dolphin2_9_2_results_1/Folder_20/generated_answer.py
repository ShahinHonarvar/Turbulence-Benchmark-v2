def gcf_three_nums(list_of_numbers):
    num1 = list_of_numbers[29]
    num2 = list_of_numbers[53]
    num3 = list_of_numbers[42]
    factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)