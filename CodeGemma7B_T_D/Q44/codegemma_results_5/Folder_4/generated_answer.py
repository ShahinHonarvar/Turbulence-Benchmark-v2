def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(56, 99):
        if numbers[i] % 2 == 0 or numbers[i] % 3 == 0 or numbers[i] % 5 == 0:
            composite_nums.add(numbers[i])
    return composite_nums