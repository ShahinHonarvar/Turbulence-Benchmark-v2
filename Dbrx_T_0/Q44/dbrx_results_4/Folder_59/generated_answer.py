def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(9, len(numbers) - 1)):
        if numbers[i] > 1 and (not (numbers[i] == 2 or numbers[i] == 3 or (numbers[i] % 2 != 0 and numbers[i] % 3 != 0))):
            composite_numbers.add(numbers[i])
    return composite_numbers