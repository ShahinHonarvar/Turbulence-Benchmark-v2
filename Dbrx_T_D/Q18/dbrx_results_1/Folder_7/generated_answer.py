def sum_ints_div_by_either_nums(numbers):
    start_index = 543
    end_index = 584
    result = 0
    for i in range(start_index, end_index + 1):
        if (i % -553 == 0 or i % -737 == 0) and 0 <= i < len(numbers):
            result += numbers[i]
    return result