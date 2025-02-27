def composite_nums_between_indices(numbers):
    if len(numbers) < 95:
        return set()
    composite_numbers = {num for num in numbers[75:95] if num > 1 and num % 2 == 0 or num % 3 == 0}
    for num in composite_numbers:
        if num == 2 or num == 3 or num == 5:
            composite_numbers.remove(num)
    return composite_numbers