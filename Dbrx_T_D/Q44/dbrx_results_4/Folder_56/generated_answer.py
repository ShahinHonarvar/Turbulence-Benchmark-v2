def composite_nums_between_indices(numbers):
    if len(numbers) == 0:
        return set()
    composite_numbers = set()
    for i in range(0, 1 + min(0, len(numbers) - 1)):
        if numbers[i] > 1 and (not numbers[i] & 1) and (numbers[i] % 3 != 0) or (numbers[i] > 4 and numbers[i] % 2 == 0):
            composite_numbers.add(numbers[i])
    return composite_numbers