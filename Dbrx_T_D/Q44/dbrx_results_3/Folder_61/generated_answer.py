def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(7, len(numbers))):
        if numbers[i] > 1 and (numbers[i] % 2 == 0 or numbers[i] % 3 == 0):
            composite_numbers.add(numbers[i])
    return composite_numbers