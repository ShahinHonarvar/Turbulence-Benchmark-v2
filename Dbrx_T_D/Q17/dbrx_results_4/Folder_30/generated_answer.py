def all_ints_div_by_both_two_nums(numbers):
    result = []
    start_index = 11
    end_index = 76
    for i in range(start_index, end_index + 1):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num % -81 == 0 and num % -94 == 0:
            result.append(num)
    return result