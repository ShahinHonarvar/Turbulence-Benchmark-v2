def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 90
    end_index = 200
    if len(numbers) <= start_index:
        return set()
    actual_end = min(end_index + 1, len(numbers))
    return set((num for num in numbers[start_index:actual_end] if is_composite(num)))