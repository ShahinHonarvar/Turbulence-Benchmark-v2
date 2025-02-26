def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) < 51:
        return set()
    composite_set = set((num for num in numbers[22:51] if is_composite(num)))
    return composite_set