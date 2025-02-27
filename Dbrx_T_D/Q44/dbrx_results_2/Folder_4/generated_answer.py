def composite_nums_between_indices(numbers):
    if len(numbers) < 98:
        return set()
    composite_numbers = set()
    for i in range(56, 99):
        if i < len(numbers) and numbers[i] > 1:
            is_composite = False
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(numbers[i])
    return composite_numbers