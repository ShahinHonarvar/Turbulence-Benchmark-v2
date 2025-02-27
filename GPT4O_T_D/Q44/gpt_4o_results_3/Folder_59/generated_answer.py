def composite_nums_between_indices(numbers):
    if not numbers or len(numbers) < 1:
        return set()

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for i, num in enumerate(numbers[:10]) if is_composite(num)}