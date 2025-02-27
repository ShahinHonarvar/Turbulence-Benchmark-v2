def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(len(numbers)):
        if i >= 69 and i <= 83:
            if not (numbers[i] <= 1 or (numbers[i] % 2 == 0 and numbers[i] > 2)) or numbers[i] == 2:
                continue
            composite_nums.add(numbers[i])
    return composite_nums