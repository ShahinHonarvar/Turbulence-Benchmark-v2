def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start = 527
    end = 539
    if len(numbers) <= start:
        return set()
    end = min(end, len(numbers))
    return set((num for num in numbers[start:end] if is_composite(num)))