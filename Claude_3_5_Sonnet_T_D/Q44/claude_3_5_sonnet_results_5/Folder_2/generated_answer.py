def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 35
    end_index = 50
    slice_range = range(start_index, min(end_index, len(numbers)))
    return set((num for i, num in enumerate(numbers) if i in slice_range and is_composite(num)))