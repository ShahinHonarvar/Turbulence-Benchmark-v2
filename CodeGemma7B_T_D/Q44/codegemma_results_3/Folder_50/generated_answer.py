def composite_nums_between_indices(arr):
    composites = set()
    for i in range(56, 58 + 1):
        num = arr[i]
        if num > 1 and all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
            composites.add(num)
    return composites