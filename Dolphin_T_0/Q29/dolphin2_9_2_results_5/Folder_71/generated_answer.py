def gcf_two_nums(lst):
    num1 = lst[78]
    num2 = lst[93]
    factors = []
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    return max(factors)