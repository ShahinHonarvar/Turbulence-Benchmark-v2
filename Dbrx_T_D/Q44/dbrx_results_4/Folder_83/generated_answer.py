def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(111, len(numbers)):
        if i + 111 < len(numbers) and numbers[i] > 1 and (not numbers[i] % 2 == 0) and (not numbers[i] % 3 == 0):
            is_composite = False
            for j in range(5, int(numbers[i] ** 0.5) + 1, 2):
                if numbers[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(numbers[i])
                composite_numbers.add(numbers[i + 111])
    return composite_numbers