def composite_nums_between_indices(numbers):
    if len(numbers) < 10:
        return set()
    composite_numbers = {num for i, num in enumerate(numbers) if i >= 8 and i <= 9 and (num > 1) and (not num.is_prime())}
    return composite_numbers