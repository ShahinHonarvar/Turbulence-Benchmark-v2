def composite_nums_between_indices(numbers):
    if len(numbers) < 93:
        return set()
    composite_numbers = {num for num in numbers[62:93] if num > 1 and (not num == 2) and all((num % i != 0 for i in range(2, num)))}
    return composite_numbers