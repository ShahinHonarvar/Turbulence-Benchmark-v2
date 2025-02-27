def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(1, min(5, len(numbers))):
        if numbers[i] > 1 and (not (numbers[i] & 1 and numbers[i] % 3 != 0)):
            composite_numbers.add(numbers[i])
    return composite_numbers