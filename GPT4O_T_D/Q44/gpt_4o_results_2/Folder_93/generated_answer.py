def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) <= 23:
        return set()
    result = set()
    for i in range(23, min(24, len(numbers))):
        if is_composite(numbers[i]):
            result.add(numbers[i])
    return result