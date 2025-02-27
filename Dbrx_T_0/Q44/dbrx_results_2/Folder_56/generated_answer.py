def composite_nums_between_indices(numbers):
    if len(numbers) < 2:
        return set()
    composite_numbers = set()
    for i in range(1, 2):
        for j in range(i, len(numbers)):
            if j > i and numbers[j] % 2 == 0 and (numbers[j] > 1):
                composite_numbers.add(numbers[j])
    return composite_numbers