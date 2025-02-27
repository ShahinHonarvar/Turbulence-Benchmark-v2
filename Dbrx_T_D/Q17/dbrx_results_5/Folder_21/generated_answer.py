def all_ints_div_by_both_two_nums(numbers):
    start_index = 315
    end_index = 934
    result = []
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and numbers[i] % -897 == 0 and (numbers[i] % -556 == 0):
            result.append(numbers[i])
    return result