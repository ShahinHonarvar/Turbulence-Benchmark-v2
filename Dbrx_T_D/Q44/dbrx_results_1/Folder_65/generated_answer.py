def composite_nums_between_indices(numbers):
    if len(numbers) < 87:
        return set()
    composite_numbers = set()
    for i in range(82, 87):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num > 1 and (not (num == 2 or (num % 2 == 1 and num % 3 == 1))):
            composite_numbers.add(num)
    return composite_numbers