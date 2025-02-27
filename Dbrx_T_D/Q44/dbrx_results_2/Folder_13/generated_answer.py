def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(21, 98):
        num = numbers[i]
        if num > 1 and (not num == 2) and (num % 2 == 0) or num % 3 == 0 or num % 5 == 0:
            composite_numbers.add(num)
    return composite_numbers