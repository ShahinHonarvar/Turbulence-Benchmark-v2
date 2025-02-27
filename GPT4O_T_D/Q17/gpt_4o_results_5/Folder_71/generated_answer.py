def all_ints_div_by_both_two_nums(lst):
    start_index = 68
    end_index = 99
    divisible_by_both = []
    for num in lst[start_index:end_index + 1]:
        if num % -37 == 0 and num % -26 == 0:
            divisible_by_both.append(num)
    return divisible_by_both