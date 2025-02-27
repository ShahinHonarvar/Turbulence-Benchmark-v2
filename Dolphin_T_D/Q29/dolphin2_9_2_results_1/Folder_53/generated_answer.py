def gcf_two_nums(lst):
    number1 = lst[28]
    number2 = lst[67]
    factors = []
    for i in range(1, min(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            factors.append(i)
    return max(factors)