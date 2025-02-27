def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(max(70, 0), min(201, len(numbers))):
        num = numbers[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers