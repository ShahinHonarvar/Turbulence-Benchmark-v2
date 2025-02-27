def composite_nums_between_indices(numbers):
    if len(numbers) < 200:
        return set()
    composite_numbers = set()
    for i in range(80, 201):
        num = numbers[i]
        if num > 1 and (not (num & 1 and num % 3 == 0)):
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                composite_numbers.add(num)
    return composite_numbers