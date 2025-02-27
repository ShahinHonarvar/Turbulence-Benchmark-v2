def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(1, 6):
        if i < len(numbers) and numbers[i] > 1 and (not numbers[i] & 1) and (numbers[i] % 3 != 0 or numbers[i] == 3) or (numbers[i] % 5 != 0 or numbers[i] == 5):
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    break
            else:
                composite_numbers.add(numbers[i])
    return composite_numbers