def gcf_three_nums(numbers):
    num1 = numbers[46]
    num2 = numbers[84]
    num3 = numbers[23]
    factors = set([i for i in range(1, max(num1, num2, num3)) if num1 % i == num2 % i == num3 % i == 0])
    return max(factors)