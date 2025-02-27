def composite_nums_between_indices(numbers):
    composites = set()
    for num in numbers[29:94]:
        if num % 2 != 0 and num not in [2, 3, 5, 7]:
            for divisor in range(3, int(num ** 0.5) + 1, 2):
                if num % divisor == 0:
                    composites.add(num)
    return composites