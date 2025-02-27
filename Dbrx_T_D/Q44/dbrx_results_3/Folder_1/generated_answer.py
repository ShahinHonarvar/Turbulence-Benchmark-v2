def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Input must be a list')
    if len(numbers) < 84:
        return set()
    result = set()
    for i in range(69, 84):
        num = numbers[i]
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num > 2))):
            result.add(num)
    return result