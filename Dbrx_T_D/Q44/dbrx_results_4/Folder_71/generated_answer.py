def composite_nums_between_indices(numbers):
    if len(numbers) < 98:
        return set()
    composite_numbers = set()
    for i in range(59, 98):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num > 1 and (not num & 1):
            composite_numbers.add(num)
    return composite_numbers