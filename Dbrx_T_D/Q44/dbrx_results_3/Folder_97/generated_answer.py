def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i < 15 or i > 39:
            continue
        if numbers[i] <= 1:
            continue
        is_composite = True
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_composite = False
                break
        if is_composite:
            composite_numbers.add(numbers[i])
    return composite_numbers