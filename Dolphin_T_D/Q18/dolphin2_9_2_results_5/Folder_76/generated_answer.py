def sum_ints_div_by_either_nums(lst):
    sum = 0
    for num in lst[250:630]:
        if num % 850 == 0 or num % 587 == 0:
            sum += num
    return sum if sum != 0 else 0