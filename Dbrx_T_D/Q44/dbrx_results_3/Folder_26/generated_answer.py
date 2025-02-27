def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or len(numbers) < 51:
        return set()
    composite_nums = set()
    for i in range(22, 51):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num < 2 or (num % 2 == 0 and num > 2):
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums