def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) < 69:
        return set()
    composite_range = numbers[42:69]
    return {num for num in composite_range if is_composite(num)}