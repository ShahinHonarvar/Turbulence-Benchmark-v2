def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites = set()
    if 222 < len(numbers):
        for i in range(222, min(223, len(numbers))):
            if is_composite(numbers[i]):
                composites.add(numbers[i])
    return composites