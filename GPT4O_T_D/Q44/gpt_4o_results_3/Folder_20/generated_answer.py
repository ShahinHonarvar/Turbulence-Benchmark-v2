def composite_nums_between_indices(numbers):
    if len(numbers) < 96:
        return set()

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return {num for num in numbers[74:96] if is_composite(num)}