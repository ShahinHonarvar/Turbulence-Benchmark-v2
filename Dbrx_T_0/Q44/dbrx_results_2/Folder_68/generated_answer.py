def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(8, len(numbers))):
        if i < 0 or i > 8:
            continue
        num = numbers[i]
        if num > 1 and num % 2 == 0 or num % 3 == 0:
            composite_numbers.add(num)
    return composite_numbers