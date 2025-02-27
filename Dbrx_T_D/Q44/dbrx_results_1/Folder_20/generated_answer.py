def composite_nums_between_indices(numbers):
    if len(numbers) < 96:
        return set()
    composite_numbers = {n for n in numbers[74:96] if n > 1 and (not all((n % i for i in range(2, n))))}
    return composite_numbers