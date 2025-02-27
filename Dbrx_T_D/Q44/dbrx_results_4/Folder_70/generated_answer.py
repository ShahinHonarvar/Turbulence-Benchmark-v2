def composite_nums_between_indices(numbers):
    if len(numbers) < 36:
        return set()
    composite_numbers = set()
    for num in numbers[32:36]:
        if num > 1 and (not (num & 1 or num % 3)) or any((num % i == 0 for i in range(4, int(num ** 0.5) + 1, 2))):
            composite_numbers.add(num)
    return composite_numbers