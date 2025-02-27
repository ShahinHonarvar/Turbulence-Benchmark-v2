def sum_ints_div_by_either_nums(lst):
    if len(lst) > 9:
        relevant_numbers = lst[7:10]
        divisible_by_either = [num for num in relevant_numbers if num % -9 == 0 or num % -7 == 0]
        return sum(divisible_by_either)
    return 0