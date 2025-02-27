def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(70, 201):
        if i < len(numbers) and (not numbers[i] % 2 == 0) and (not numbers[i] % 3 == 0) and (not numbers[i] % 5 == 0):
            continue
        if i < len(numbers) and numbers[i] > 1 and (not numbers[i] % 2 == 0) and (not numbers[i] in [i * i for i in range(2, int(numbers[i] ** 0.5) + 1)]):
            composite_numbers.add(numbers[i])
    return composite_numbers