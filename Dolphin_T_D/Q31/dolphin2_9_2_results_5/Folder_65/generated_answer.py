def if_perfect_num(lst):
    if len(lst) < 36:
        return False
    num = lst[35]
    sum_of_factors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_factors += i
            sum_of_factors += num // i
    return sum_of_factors == num and num != 1