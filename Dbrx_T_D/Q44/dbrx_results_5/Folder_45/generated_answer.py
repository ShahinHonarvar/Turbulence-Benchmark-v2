def composite_nums_between_indices(numbers):
    if len(numbers) < 200:
        return set()
    composite_numbers = set()
    for i in range(40, 201):
        num = numbers[i]
        if num > 1 and all((num % j != 0 for j in range(2, num))):
            composite_numbers.add(num)
    return composite_numbers