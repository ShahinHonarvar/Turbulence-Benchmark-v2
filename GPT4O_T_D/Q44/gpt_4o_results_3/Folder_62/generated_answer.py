def composite_nums_between_indices(numbers):
    if len(numbers) < 31:
        return set()

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {numbers[i] for i in range(30, min(88, len(numbers))) if is_composite(numbers[i])}