def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = max(90, 0)
    end_index = min(200, len(numbers) - 1)
    composites = set()
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and is_composite(numbers[i]):
            composites.add(numbers[i])
    return composites