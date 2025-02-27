def composite_nums_between_indices(numbers):
    if len(numbers) < 605:
        return set()
    composite_numbers = set()
    for i in range(533, 606):
        num = numbers[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            composite_numbers.add(num)
        elif num > 1 and num % 2 != 0:
            for j in range(3, int(num ** 0.5) + 1, 2):
                if num % j == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers