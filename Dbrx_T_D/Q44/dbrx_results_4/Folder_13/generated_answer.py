def composite_nums_between_indices(numbers):
    if not numbers or len(numbers) < 97:
        return set()
    composite_numbers = set()
    for i in range(21, 98):
        if numbers[i] > 1 and (not (numbers[i] == 2 or numbers[i] == 3 or numbers[i] == 5 or (numbers[i] == 7))):
            is_composite = False
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(numbers[i])
    return composite_numbers