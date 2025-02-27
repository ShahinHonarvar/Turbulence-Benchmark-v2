def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or len(numbers) < 86:
        return set()
    composite_numbers = set()
    for num in numbers[75:86]:
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num > 2))):
            is_composite = False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(num)
    return composite_numbers