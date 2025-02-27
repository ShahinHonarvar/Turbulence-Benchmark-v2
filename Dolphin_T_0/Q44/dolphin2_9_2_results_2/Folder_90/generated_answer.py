def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(333, 369):
        number = numbers[i]
        if all((number % j != 0 for j in range(2, int(number ** 0.5) + 1))):
            continue
        composite_numbers.add(number)
    return composite_numbers