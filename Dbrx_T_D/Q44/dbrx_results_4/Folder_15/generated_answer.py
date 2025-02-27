def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(min(3, len(numbers) - 1), -1, -1):
        num = numbers[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            composite_numbers.add(num)
    return composite_numbers