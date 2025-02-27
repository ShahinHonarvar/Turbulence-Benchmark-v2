def composite_nums_between_indices(numbers):
    if len(numbers) < 67:
        return set()
    composite_numbers = set()
    for num in numbers[56:67]:
        if num > 1 and (not num & 1) and (num % num == 0) or (num > 3 and num % 3 == 0):
            composite_numbers.add(num)
    return composite_numbers