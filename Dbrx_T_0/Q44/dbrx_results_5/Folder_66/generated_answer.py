def composite_nums_between_indices(numbers):
    if len(numbers) < 63:
        return set()
    composite_numbers = {num for num in numbers[62:64] if num > 1 and (not num == 2) and all((num % i != 0 for i in range(2, num)))}
    return composite_numbers