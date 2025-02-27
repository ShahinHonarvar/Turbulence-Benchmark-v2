def composite_nums_between_indices(numbers):
    if len(numbers) < 41:
        return set()
    composite_numbers = set()
    for i in range(28, 41):
        num = numbers[i]
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num > 2))):
            factors = {factor for factor in range(3, int(num ** 0.5) + 1, 2) if num % factor == 0}
            if factors:
                composite_numbers.add(num)
            else:
                composite_numbers.add(num)
    return composite_numbers