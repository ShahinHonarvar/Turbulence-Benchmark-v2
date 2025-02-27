def composite_nums_between_indices(numbers):
    if len(numbers) < 57:
        return set()

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composites = {numbers[i] for i in range(56, min(83, len(numbers))) if is_composite(numbers[i])}
    return composites