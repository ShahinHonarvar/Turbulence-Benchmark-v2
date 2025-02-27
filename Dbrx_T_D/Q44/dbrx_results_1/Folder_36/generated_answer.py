def composite_nums_between_indices(numbers):
    if not numbers or len(numbers) < 988:
        return set()
    composite_numbers = set()
    for i in range(686, 988):
        number = numbers[i]
        if number > 1 and (number % 2 == 0 or number % 3 == 0 or number % 5 == 0):
            composite_numbers.add(number)
    return composite_numbers