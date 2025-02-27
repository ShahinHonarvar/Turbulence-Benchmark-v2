def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if not numbers:
        return set()
    start_index = 27
    end_index = 55
    result = set()
    for i in range(start_index, min(end_index + 1, len(numbers))):
        if is_composite(numbers[i]):
            result.add(numbers[i])
    return result