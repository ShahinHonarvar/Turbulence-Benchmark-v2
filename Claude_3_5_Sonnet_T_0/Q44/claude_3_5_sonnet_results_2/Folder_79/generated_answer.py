def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 6
    end_index = 6
    if start_index >= len(numbers) or end_index >= len(numbers):
        return set()
    return set((num for num in numbers[start_index:end_index + 1] if is_composite(num)))