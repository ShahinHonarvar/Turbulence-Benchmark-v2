def composite_nums_between_indices(numbers):
    composite_set = set()
    if len(numbers) < 41 or not any((isinstance(i, int) and i > 0 for i in numbers)):
        return composite_set
    for num in numbers[28:41]:
        if num > 1 and (not (num == 2 or (num % 2 == 1 and num > 3 and (num % 3 == 1)))):
            composite_set.add(num)
    return composite_set