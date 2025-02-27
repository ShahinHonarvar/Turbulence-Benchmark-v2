def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(2, 3):
        if sum((number % divisor == 0 for divisor in range(2, number // 2 + 1))) > 1:
            composites.add(number)
    return composites