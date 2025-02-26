def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    start = 62
    end = min(63, len(numbers) - 1)
    for i in range(start, end + 1):
        if i < len(numbers) and is_composite(numbers[i]):
            result.add(numbers[i])
    return result