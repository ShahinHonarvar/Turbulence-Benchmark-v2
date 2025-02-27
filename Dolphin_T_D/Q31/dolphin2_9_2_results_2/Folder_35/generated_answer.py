def if_perfect_num(lst):
    perfect_number = lst[993]
    sum_of_factors = 1
    i = 2
    while i * i <= perfect_number:
        if perfect_number % i:
            i += 1
        elif i * (perfect_number // i) == perfect_number:
            sum_of_factors = sum_of_factors + i
            i += 1
        else:
            sum_of_factors = sum_of_factors + (i + perfect_number // i)
            i += 1
    return sum_of_factors == perfect_number