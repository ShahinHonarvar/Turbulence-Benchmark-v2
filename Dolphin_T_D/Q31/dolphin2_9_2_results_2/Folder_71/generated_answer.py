def if_perfect_num(lst):
    index_78 = lst[78]
    sum_of_factors = 0
    for i in range(1, index_78):
        if index_78 % i == 0:
            sum_of_factors += i
    if sum_of_factors == index_78:
        return True
    return False