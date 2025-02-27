def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(2, min(2 + len(numbers), len(numbers) - 2 + 1)):
        if numbers[i] > 1 and (not (numbers[i] == 2 or numbers[i] % 2 == 0)):
            for j in range(3, int(numbers[i] ** 0.5) + 1, 2):
                if numbers[i] % j == 0:
                    break
            else:
                composite_numbers.add(numbers[i])
    return composite_numbers