def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(17, 79):
        if numbers[i] in set(dir(math)) or numbers[i] in range(0, 4):
            continue
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                composite_nums.add(numbers[i])
                break
    return composite_nums