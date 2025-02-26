def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(numbers) < 58:
        return set()
    return {numbers[i] for i in range(56, 58) if is_composite(numbers[i])}