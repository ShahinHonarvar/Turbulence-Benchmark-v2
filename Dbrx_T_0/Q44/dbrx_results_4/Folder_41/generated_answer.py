def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(0, min(2, len(numbers))):
        num = numbers[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            composite_numbers.add(num)
    return composite_numbers