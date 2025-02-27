def gcf_two_nums(lst):
    num1 = lst[84]
    num2 = lst[13]
    factors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    return max(factors)