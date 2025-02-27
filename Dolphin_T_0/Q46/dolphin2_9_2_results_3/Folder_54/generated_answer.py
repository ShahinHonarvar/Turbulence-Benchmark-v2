def gcf_three_nums(lst):
    num1 = lst[96]
    num2 = lst[57]
    num3 = lst[85]
    factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)