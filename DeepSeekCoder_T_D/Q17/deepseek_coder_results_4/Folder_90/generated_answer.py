def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[138:425]:
        if num % -863 == 0 and num % -329 == 0:
            result.append(num)
    return result