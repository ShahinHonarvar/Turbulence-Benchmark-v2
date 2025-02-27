def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(56, 99):
        if i < len(numbers) and numbers[i] > 1 and (not numbers[i] % 2 == 0) and (not numbers[i] % 3 == 0):
            composite_numbers.add(numbers[i])
    return composite_numbers