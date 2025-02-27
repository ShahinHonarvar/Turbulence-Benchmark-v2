def composite_nums_between_indices(numbers):
    if len(numbers) < 73:
        return set()
    composite_numbers = set()
    for i in range(31, 73):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            if all((num % j != 0 for j in range(5, int(num ** 0.5) + 1, 2))):
                composite_numbers.add(num)
        elif num > 1 and num % 2 == 0:
            if all((num % j != 0 for j in range(3, int(num ** 0.5) + 1, 2))):
                composite_numbers.add(num)
    return composite_numbers