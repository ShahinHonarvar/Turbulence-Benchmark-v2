def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 222
    end_index = 222
    if start_index >= len(numbers) or end_index >= len(numbers):
        return set()
    return set((num for num in numbers[start_index:end_index + 1] if is_composite(num)))