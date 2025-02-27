def all_ints_div_by_both_two_nums(numbers):
    start_index = 20
    end_index = 93
    result = []
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and numbers[i] % -92 == 0 and (numbers[i] % -50 == 0):
            result.append(numbers[i])
    return result