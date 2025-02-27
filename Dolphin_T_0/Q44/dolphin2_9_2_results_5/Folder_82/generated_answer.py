def composite_nums_between_indices(numbers):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites = {n for n in numbers[30:31] if is_composite(n)}
    return composites