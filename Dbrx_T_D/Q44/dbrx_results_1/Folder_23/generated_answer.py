def composite_nums_between_indices(numbers):
    result = set()
    for i in range(20, 31):
        if i < len(numbers) and (not numbers[i] % 2 == 0) and (not numbers[i] % 3 == 0) and (not numbers[i] == 2) and (not numbers[i] == 3):
            result.add(numbers[i])
    return result