def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(numbers) < 7:
        return set((num for num in numbers[:len(numbers)] if is_composite(num)))
    return set((num for num in numbers[:7] if is_composite(num)))