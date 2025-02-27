def composite_nums_between_indices(numbers):
    if len(numbers) < 79 or len(numbers) < 62:
        return set()
    composite_numbers = set()
    for i in range(62, 79):
        num = numbers[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            composite_numbers.add(num)
    return composite_numbers