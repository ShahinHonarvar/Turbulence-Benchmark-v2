def composite_nums_between_indices(numbers):
    if len(numbers) < 3:
        return set()
    composite_numbers = set()
    for num in numbers[:3]:
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            composite_numbers.add(num)
    return composite_numbers - set([2])