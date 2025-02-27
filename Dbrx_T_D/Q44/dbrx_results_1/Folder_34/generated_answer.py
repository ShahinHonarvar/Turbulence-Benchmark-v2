def composite_nums_between_indices(numbers):
    if len(numbers) < 201:
        return set()
    result = set()
    for i in range(70, 201):
        num = numbers[i]
        if num > 1 and (not any((num % j == 0 for j in range(2, num)))):
            result.add(num)
    return result