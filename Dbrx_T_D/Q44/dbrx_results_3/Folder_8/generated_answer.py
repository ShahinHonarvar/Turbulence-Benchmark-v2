def composite_nums_between_indices(numbers):
    if len(numbers) < 87:
        return set()
    composite_nums = {num for num in numbers[68:87] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums