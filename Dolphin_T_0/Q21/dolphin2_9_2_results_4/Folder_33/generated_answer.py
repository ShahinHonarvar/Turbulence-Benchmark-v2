def all_ints_div_by_num(lst):
    divisible_numbers = []
    for num in lst[319:613]:
        if num % -215 == 0:
            divisible_numbers.append(num)
    return divisible_numbers