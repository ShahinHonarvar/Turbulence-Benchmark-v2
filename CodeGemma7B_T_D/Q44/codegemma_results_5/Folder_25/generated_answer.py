def composite_nums_between_indices(composites):
    result = set()
    for i, num in enumerate(composites[75:95]):
        if num > 1 and all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
            result.add(num)
    return result