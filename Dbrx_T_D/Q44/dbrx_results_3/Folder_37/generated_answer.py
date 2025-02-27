def composite_nums_between_indices(numbers):
    if len(numbers) < 6:
        return set()
    composite_numbers = set()
    for num in numbers[0:6]:
        if num > 1 and num % 2 == 0:
            composite_numbers.add(num)
    return composite_numbers