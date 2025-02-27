def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(2, len(numbers)), min(3, len(numbers)) + 1):
        if numbers[i] > 1 and (not numbers[i] == 2) and (numbers[i] % 2 != 0):
            is_composite = False
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(numbers[i])
    return composite_numbers