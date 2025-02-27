def composite_nums_between_indices(numbers):
    result = set()
    if len(numbers) > 1:
        for i in range(1, min(2, len(numbers))):
            if numbers[i] > 1 and numbers[i] % 2 == 0:
                result.add(numbers[i])
    return result