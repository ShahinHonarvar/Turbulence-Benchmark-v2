def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i < 22 or i > 50:
            continue
        if i > 50:
            break
        if numbers[i] <= 1:
            continue
        is_composite = False
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_numbers.add(numbers[i])
    return composite_numbers