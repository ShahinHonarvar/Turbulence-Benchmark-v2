def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    end_index = min(8, len(numbers) - 1)
    return set((num for num in numbers[:end_index + 1] if is_composite(num)))