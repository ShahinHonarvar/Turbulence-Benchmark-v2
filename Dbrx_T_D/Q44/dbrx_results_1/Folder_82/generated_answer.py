def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 30 and i <= 49 and (numbers[i] > 1):
            if numbers[i] > 2 and numbers[i] % 2 == 0 or numbers[i] % 3 == 0:
                composite_numbers.add(numbers[i])
    return composite_numbers