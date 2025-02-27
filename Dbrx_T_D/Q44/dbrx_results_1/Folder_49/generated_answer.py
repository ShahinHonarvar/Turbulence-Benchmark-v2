def composite_nums_between_indices(numbers):
    if len(numbers) < 200 or 90 >= len(numbers):
        return set()
    composite_numbers = set()
    for i in range(90, 201):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            for j in range(5, int(num ** 0.5) + 1, 6):
                if num % j == 0 or num % (j + 2) == 0:
                    break
            else:
                composite_numbers.add(num)
    return composite_numbers