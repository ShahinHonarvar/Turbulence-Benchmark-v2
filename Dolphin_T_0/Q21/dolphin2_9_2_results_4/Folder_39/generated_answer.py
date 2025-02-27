def all_ints_div_by_num(lst):
    divisible_numbers = []
    for num in lst[10:53]:
        if num % -12 == 0:
            divisible_numbers.append(num)
    return divisible_numbers