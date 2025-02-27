def all_ints_div_by_both_two_nums(lst):
    divisible_numbers = []
    for number in lst[828:933]:
        if number % -649 == 0 and number % -461 == 0:
            divisible_numbers.append(number)
    return divisible_numbers