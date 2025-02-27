def composite_nums_between_indices(numbers):
    if len(numbers) < 53:
        return set()
    composite_numbers = set()
    for i in range(26, 53):
        num = numbers[i]
        if num > 1 and (not num.is_prime()):
            composite_numbers.add(num)
    return composite_numbers