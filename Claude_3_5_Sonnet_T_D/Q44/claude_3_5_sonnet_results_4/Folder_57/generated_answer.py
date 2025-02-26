def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 25
    end_index = 60
    if len(numbers) <= start_index:
        return set()
    range_end = min(end_index, len(numbers))
    return set((num for num in numbers[start_index:range_end] if is_composite(num)))