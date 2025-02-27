def composite_nums_between_indices(numbers):
    if len(numbers) < 200:
        return set()
    composite_numbers = set()
    for i in range(70, 201):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num % 3 != 0) or (num > 3 and num % 5 != 0):
            composite_numbers.add(num)
    return composite_numbers