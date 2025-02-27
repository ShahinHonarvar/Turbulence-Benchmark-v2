def all_ints_div_by_num(numbers):
    start_index = 20
    end_index = 20
    div_by_num = 2
    result = []
    if end_index < len(numbers) and end_index >= 0:
        for i in range(start_index, end_index + 1):
            if numbers[i] % div_by_num == 0:
                result.append(numbers[i])
    return result