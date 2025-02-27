def all_ints_not_div_by_num(numbers):
    start_index = 41
    end_index = 69
    result = []
    for i in range(start_index, end_index):
        if numbers[i] % -82 != 0:
            result.append(numbers[i])
    return result