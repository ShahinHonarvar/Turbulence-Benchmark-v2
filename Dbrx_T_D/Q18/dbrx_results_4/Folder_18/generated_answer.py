def sum_ints_div_by_either_nums(numbers):
    start_index = 55
    end_index = 66
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and (numbers[i] % 22 == 0 or numbers[i] % 82 == 0):
            sum += numbers[i]
    return sum