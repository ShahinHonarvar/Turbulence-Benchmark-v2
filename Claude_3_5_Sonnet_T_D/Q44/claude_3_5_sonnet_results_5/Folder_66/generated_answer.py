def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 62
    end_index = 63
    if len(numbers) <= start_index:
        return set()
    range_end = min(end_index + 1, len(numbers))
    return set((num for num in numbers[start_index:range_end] if is_composite(num)))