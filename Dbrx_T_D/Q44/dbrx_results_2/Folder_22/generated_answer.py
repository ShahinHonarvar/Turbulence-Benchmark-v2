def composite_nums_between_indices(numbers):
    result = set()
    for i in range(len(numbers)):
        if i < 50 or i > 200:
            continue
        if i == 50 and (not any((num < 2 for num in numbers[:50]))):
            continue
        if i == 200 and (not any((num < 2 or num > 200 for num in numbers[200:]))):
            continue
        if numbers[i] < 2:
            continue
        is_composite = False
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            result.add(numbers[i])
    return result