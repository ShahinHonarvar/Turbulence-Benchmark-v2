def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = max(60, 0)
    end_index = min(200, len(numbers) - 1)
    return set((num for num in numbers[start_index:end_index + 1] if is_composite(num)))