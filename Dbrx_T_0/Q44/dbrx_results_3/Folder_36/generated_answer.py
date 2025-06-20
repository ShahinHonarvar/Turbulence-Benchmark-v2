def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(686, 988):
        if i < len(numbers) and numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    composite_numbers.add(numbers[i])
                    break
    return composite_numbers