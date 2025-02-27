def composite_nums_between_indices(numbers):
    if len(numbers) < 8:
        return set()
    result = set()
    for num in numbers[5:8]:
        if num > 1 and (not num & 1) and (num % 3 != 0) or num % 5 == 0:
            result.add(num)
    return result