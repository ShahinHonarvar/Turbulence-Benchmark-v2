def composite_nums_between_indices(numbers):
    if len(numbers) < 78:
        return set()
    composite_numbers = set()
    for i in range(17, 79):
        num = numbers[i]
        if num > 1:
            if any((num % j == 0 for j in range(2, num))):
                composite_numbers.add(num)
    return composite_numbers