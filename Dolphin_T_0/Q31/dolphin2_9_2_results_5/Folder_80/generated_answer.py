def if_perfect_num(lst):
    num = lst[746]
    sum_factors = 0
    i = 1
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum_factors = sum_factors + i
            i += 1
        else:
            sum_factors = sum_factors + (i + num // i)
            i += 1
    return sum_factors == num and num != 1