def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(56, 99):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num < 2 or (num % 2 == 0 and num != 2 and (num != 4)) or (num % 3 == 0 and num != 3):
            composite_set.add(num)
    return composite_set