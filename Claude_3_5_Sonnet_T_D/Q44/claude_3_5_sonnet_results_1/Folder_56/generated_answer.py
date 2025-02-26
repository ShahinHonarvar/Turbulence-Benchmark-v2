def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composites = set()
    if len(numbers) > 0:
        if is_composite(numbers[0]):
            composites.add(numbers[0])
    return composites