def composite_nums_between_indices(numbers):
    if len(numbers) < 55:
        return set()
    composite_numbers = set()
    for num in numbers[50:55]:
        if num > 1 and num % 2 == 0:
            composite_numbers.add(num)
        elif num > 3 and num % 3 == 0:
            composite_numbers.add(num)
    return composite_numbers