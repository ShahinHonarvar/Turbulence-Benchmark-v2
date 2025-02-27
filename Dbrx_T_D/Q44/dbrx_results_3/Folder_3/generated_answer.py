def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i < 66 or i > 93:
            continue
        if i > 0 and numbers[i] % (i + 1) == 0 and (numbers[i] != i + 1):
            composite_numbers.add(numbers[i])
    return composite_numbers