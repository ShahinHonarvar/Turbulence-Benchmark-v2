def gcf_three_nums(numbers):
    num1 = numbers[96]
    num2 = numbers[57]
    num3 = numbers[85]
    factors = []
    for i in range(1, max(num1, num2, num3) + 1):
        if num1 % i == num2 % i == num3 % i == 0:
            factors.append(i)
    return max(factors)