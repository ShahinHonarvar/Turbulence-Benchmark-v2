def composite_nums_between_indices(numbers):
    if len(numbers) < 201 or len(numbers) < 20:
        return set()
    composite_numbers = set()
    for i in range(20, 201):
        if numbers[i] > 1 and numbers[i] % 2 == 0:
            composite_numbers.add(numbers[i])
        elif numbers[i] > 1:
            for j in range(3, int(numbers[i] ** 0.5) + 1, 2):
                if numbers[i] % j == 0:
                    composite_numbers.add(numbers[i])
                    break
    return composite_numbers