def sum_ints_div_by_either_nums(lst):
    sum = 0
    for num in lst[8:10]:
        if num % -3 == 0 or num % 6 == 0:
            sum += num
    return sum if sum != 0 else 0