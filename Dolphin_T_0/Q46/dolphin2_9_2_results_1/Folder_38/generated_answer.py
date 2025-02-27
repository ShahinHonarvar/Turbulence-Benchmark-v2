def gcf_three_nums(numbers):
    num1 = numbers[14]
    num2 = numbers[21]
    num3 = numbers[17]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    factors_all = set(factors1) & set(factors2) & set(factors3)
    return max(factors_all)