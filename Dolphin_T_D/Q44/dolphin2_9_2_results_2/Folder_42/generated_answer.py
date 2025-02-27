def composite_nums_between_indices(numbers):

    def is_composite(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(numbers) if i in range(91, 100) and is_composite(num)))