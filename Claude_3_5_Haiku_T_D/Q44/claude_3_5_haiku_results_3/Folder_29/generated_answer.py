def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) < 72:
        return set()
    return {num for num in numbers[52:72] if is_composite(num)}