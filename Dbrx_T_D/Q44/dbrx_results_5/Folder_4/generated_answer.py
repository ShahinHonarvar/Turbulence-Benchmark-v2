def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(56, 99):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            composite_numbers.add(num)
        elif num > 1 and num % 2 != 0 and any((num % x == 0 for x in range(3, int(num ** 0.5) + 1, 2))):
            composite_numbers.add(num)
    return composite_numbers