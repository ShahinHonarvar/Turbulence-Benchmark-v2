def sum_ints_div_by_either_nums(ints):
    sum = 0
    for num in ints[7:8]:
        if num % 5 == 0 or num % 7 == 0:
            sum += num
    return sum if sum != 0 else None