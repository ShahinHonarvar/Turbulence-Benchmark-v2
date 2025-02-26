def all_ints_div_by_both_two_nums(input_list):
    result = []
    for num in input_list[138:425]:
        if num % -863 == 0 and num % -329 == 0:
            result.append(num)
    return result