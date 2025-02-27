def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(max(25, 0), min(88, len(numbers))):
        num = numbers[i]
        if num > 1:
            is_composite = False
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(num)
    return composite_numbers