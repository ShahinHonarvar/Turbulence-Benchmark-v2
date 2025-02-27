def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) <= 29:
        return set()
    start, end = (29, min(93, len(numbers) - 1))
    return {num for num in numbers[start:end + 1] if is_composite(num)}