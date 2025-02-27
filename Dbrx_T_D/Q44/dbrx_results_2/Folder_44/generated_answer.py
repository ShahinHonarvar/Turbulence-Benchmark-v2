def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or len(numbers) < 67:
        return set()
    composite_set = set()
    for i in range(64, 67):
        num = numbers[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            is_composite = True
            j = 5
            limit = int(num ** 0.5)
            while j <= limit:
                if num % j == 0:
                    is_composite = False
                    break
                j += 2
            if is_composite:
                composite_set.add(num)
    return composite_set