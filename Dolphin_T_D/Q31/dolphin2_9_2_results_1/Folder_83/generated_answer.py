def if_perfect_num(lst):
    num = lst[95]
    sum_of_factors = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                sum_of_factors = sum_of_factors + i + num // i
            else:
                sum_of_factors = sum_of_factors + i
            i += 1
    return sum_of_factors == num and num != 1