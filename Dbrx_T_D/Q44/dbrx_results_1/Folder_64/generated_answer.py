def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(4, len(numbers)), max(0, min(5, len(numbers)))):
        if i == 0 or i == 1:
            continue
        is_composite = False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_numbers.add(numbers[i])
    return composite_numbers