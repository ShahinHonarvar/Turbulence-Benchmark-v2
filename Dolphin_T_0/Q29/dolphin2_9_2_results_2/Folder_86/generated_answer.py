def gcf_two_nums(lst):
    num1 = lst[793]
    num2 = lst[449]
    factors = []
    i = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
        i += 1
    return max(factors)