def composite_nums_between_indices(numbers):
    if len(numbers) < 77:
        return set()
    composite_numbers = set()
    for i in range(37, 77):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            composite_numbers.add(num)
        elif num > 3:
            for j in range(5, int(num ** 0.5) + 1, 6):
                if num % j == 0 or num % (j + 2) == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers