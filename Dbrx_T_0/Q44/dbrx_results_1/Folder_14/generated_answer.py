def composite_nums_between_indices(numbers):
    if len(numbers) < 5:
        return set()
    composite_numbers = set()
    for i in range(4, len(numbers)):
        if i < 4 or i > 4:
            continue
        num = numbers[i]
        if num < 2:
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_numbers.add(num)
    return composite_numbers