def gcf_three_nums(lst):
    num1 = lst[742]
    num2 = lst[888]
    num3 = lst[629]
    factors = [i for i in range(1, max(num1, num2, num3) + 1) if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0)]
    return max(factors)