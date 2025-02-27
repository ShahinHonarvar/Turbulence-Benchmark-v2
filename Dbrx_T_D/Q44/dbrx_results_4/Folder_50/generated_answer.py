def composite_nums_between_indices(numbers):
    if len(numbers) < 58:
        return set()
    composite_numbers = set()
    for i in range(56, 58):
        num = numbers[i]
        if num > 1 and (not (num == 2 or num == 3 or num == 5 or (num == 7))):
            if num % 2 != 0 or num == 2:
                if num % 3 != 0 or num == 3:
                    if num % 5 != 0 or num == 5:
                        if num % 7 != 0 or num == 7:
                            root = num ** 0.5
                            for j in range(9, int(root) + 1, 6):
                                if num % j == 0 or num % (j + 4) == 0:
                                    composite_numbers.add(num)
                                    break
    return composite_numbers