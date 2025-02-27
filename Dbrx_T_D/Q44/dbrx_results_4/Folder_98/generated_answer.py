def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(6, len(numbers))):
        if numbers[i] > 1 and (not (numbers[i] & 1 and numbers[i] % 3 == 0)):
            is_composite = False
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(numbers[i])
    return composite_numbers