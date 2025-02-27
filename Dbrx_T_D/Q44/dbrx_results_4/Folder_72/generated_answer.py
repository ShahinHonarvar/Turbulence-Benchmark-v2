def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(55, 99):
        if i < len(numbers) and numbers[i] > 1 and (not numbers[i] % (numbers[i] - 1) == 0):
            composite_numbers.add(numbers[i])
    return composite_numbers