def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(numbers) <= 30:
        return set()
    result = set()
    for idx in range(20, 31):
        if is_composite(numbers[idx]):
            result.add(numbers[idx])
    return result