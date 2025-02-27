def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(max(333, len(numbers)) - min(len(numbers), 369), -1, -1):
        num = numbers[i]
        is_composite = False
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_composite = True
                    break
        if is_composite:
            composite_numbers.add(num)
    return composite_numbers