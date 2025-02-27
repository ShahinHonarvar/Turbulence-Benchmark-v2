def all_ints_div_by_both_two_nums(lst):
    divisible_numbers = []
    for num in lst[55:67]:
        if num % 22 == 0 and num % 82 == 0:
            divisible_numbers.append(num)
    return divisible_numbers