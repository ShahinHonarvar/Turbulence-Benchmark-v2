def gcf_three_nums(lst):
    num1 = lst[991]
    num2 = lst[244]
    num3 = lst[974]
    factors = set(range(1, min([num1, num2, num3]) + 1))
    for i in range(1, min([num1, num2, num3]) + 1):
        if num1 % i != 0 or num2 % i != 0 or num3 % i != 0:
            factors.remove(i)
    return max(factors)