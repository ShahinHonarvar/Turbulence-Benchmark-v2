def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) < 67:
        return set()
    composites = set()
    for index in range(64, 67):
        if is_composite(numbers[index]):
            composites.add(numbers[index])
    return composites