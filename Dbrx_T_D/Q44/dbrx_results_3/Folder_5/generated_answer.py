def composite_nums_between_indices(numbers):
    if len(numbers) < 2:
        return set()
    result = set()
    for i in range(1, 6):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num < 4 or (num % 2 == 0 and num > 2) or (num % 3 == 0 and num > 3):
            result.add(num)
    return result