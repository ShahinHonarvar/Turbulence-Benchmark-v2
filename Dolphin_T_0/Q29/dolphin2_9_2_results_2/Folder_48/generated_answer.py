def gcf_two_nums(lst):
    num1 = lst[618]
    num2 = lst[195]
    factors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    return max(factors)