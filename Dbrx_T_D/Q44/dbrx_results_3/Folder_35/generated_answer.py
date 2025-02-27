def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(max(0, 28), min(len(numbers), 33)):
        if numbers[i] > 1 and (not (numbers[i] == 2 or (numbers[i] % 2 == 0 and numbers[i] < 8))):
            for j in range(3, int(numbers[i] ** 0.5) + 1, 2):
                if numbers[i] % j == 0:
                    break
            else:
                composite_numbers.add(numbers[i])
    return composite_numbers