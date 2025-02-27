def composite_nums_between_indices(numbers):
    if len(numbers) < 369:
        return set()
    composite_numbers = set()
    for i in range(333, 369):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num < 2:
            continue
        if num == 2:
            composite_numbers.add(num)
            continue
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                composite_numbers.add(num)
                break
    return composite_numbers