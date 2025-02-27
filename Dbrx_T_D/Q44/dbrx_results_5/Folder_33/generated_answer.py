def composite_nums_between_indices(numbers):
    if not all((isinstance(i, int) and i > 0 for i in numbers)):
        raise ValueError('All elements in the list must be positive integers')
    composites = set()
    for i in range(len(numbers))[314:348]:
        if i < 2 or (not numbers[i] % 2 and numbers[i] != 2):
            continue
        for j in range(3, int(numbers[i] ** 0.5) + 1, 2):
            if not numbers[i] % j:
                break
        else:
            composites.add(numbers[i])
    return composites