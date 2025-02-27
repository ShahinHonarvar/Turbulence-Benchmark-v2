def composite_nums_between_indices(numbers):
    if len(numbers) < 93:
        return set()
    composite_numbers = set()
    for i in range(66, 94):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num != 2) or (num > 3 and (not num % 3) and (num != 3)):
            composite_numbers.add(num)
    return composite_numbers