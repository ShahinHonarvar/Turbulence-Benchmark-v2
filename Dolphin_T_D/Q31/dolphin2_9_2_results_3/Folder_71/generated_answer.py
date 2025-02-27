def if_perfect_num(lst):
    num = lst[78]
    sum_of_factors = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum_of_factors = sum_of_factors + i + num // i
            i += 1
        else:
            sum_of_factors = sum_of_factors + i
            i += 1
    return sum_of_factors == num