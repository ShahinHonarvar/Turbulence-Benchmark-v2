def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 28 and i <= 40:
            if numbers[i] > 1 and (not numbers[i] % 2 == 0) and (not numbers[i] % 3 == 0):
                composite_numbers.add(numbers[i])
            elif numbers[i] > 1 and numbers[i] % 2 == 0:
                composite_numbers.add(numbers[i])
    return composite_numbers