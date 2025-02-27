def composite_nums_between_indices(numbers):
    if len(numbers) < 87:
        return set()
    composite_numbers = set()
    for num in numbers[82:87]:
        if num > 1 and (not num & 1):
            composite_numbers.add(num)
    return composite_numbers