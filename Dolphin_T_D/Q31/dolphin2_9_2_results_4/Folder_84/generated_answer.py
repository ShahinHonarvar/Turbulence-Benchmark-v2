def if_perfect_num(lst):
    num = lst[685]
    if num < 0:
        raise ValueError('Input list must contain only positive integers')
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    return sum_of_factors == num