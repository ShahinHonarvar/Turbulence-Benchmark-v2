def composite_nums_between_indices(numbers):
    if len(numbers) < 10:
        return set()
    result = set()
    for i in range(0, 10):
        if i < len(numbers):
            num = numbers[i]
            if num > 1 and (not num & 1) or (num > 3 and (not num % 3) and (num != 9)):
                result.add(num)
    return result