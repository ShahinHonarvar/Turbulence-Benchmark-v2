def composite_nums_between_indices(numbers):
    composite_set = set()
    if len(numbers) < 7:
        return composite_set
    for i in range(6, 8):
        num = numbers[i]
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num != 7))):
            composite_set.add(num)
    return composite_set