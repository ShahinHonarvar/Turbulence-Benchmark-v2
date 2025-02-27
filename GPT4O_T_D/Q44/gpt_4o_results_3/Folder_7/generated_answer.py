def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites = {n for n in numbers[527:539] if is_composite(n)}
    return composites