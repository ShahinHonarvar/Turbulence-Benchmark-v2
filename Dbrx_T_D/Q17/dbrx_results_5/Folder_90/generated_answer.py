def all_ints_div_by_both_two_nums(numbers):
    start_index = 138
    end_index = 424
    result = []
    for i in range(start_index, end_index + 1):
        if numbers[i] % -863 == 0 and numbers[i] % -329 == 0:
            result.append(numbers[i])
    return result