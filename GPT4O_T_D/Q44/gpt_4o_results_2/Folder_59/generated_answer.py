def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    end_index = min(10, len(numbers))
    return {num for num in numbers[:end_index] if is_composite(num)}