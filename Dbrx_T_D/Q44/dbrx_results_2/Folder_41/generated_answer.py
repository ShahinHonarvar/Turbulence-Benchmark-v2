def composite_nums_between_indices(numbers):
    if len(numbers) < 3:
        return set()
    result = set()
    for num in numbers[0:3]:
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            result.add(num)
    return result