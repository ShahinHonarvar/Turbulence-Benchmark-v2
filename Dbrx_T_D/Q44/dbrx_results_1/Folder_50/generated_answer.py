def composite_nums_between_indices(numbers):
    if len(numbers) < 58:
        return set()
    composite_numbers = {num for num in numbers[56:58] if num > 1 and num % 2 == 0 and (numbers[numbers.index(num) - 1] % num != 0)}
    return composite_numbers