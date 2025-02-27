def composite_nums_between_indices(numbers):
    if len(numbers) < 67:
        return set()
    result = set()
    for i in range(64, 67):
        if i < len(numbers) and numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    result.add(numbers[i])
                    break
    return result