def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(8, len(numbers)), max(0, min(9, len(numbers)))):
        if i > 0 and numbers[i] > 1 and (not numbers[i] & 1) and (numbers[i] % 3 != 0):
            composite_numbers.add(numbers[i])
    return composite_numbers