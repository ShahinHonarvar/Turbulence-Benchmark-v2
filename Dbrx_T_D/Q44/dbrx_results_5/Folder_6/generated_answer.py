def composite_nums_between_indices(numbers):
    if len(numbers) < 69 or len(numbers) < 14:
        return set()
    composite_numbers = set()
    for i in range(13, 69):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num != 2) or (num % 3 == 0 and num > 3):
            composite_numbers.add(num)
    return composite_numbers