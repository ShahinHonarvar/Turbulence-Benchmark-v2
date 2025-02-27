def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(34, 56):
        if i < len(numbers) and numbers[i] > 1 and (not numbers[i] & 1) and (numbers[i] % 3 != 0 or numbers[i] == 3):
            composite_numbers.add(numbers[i])
    return composite_numbers