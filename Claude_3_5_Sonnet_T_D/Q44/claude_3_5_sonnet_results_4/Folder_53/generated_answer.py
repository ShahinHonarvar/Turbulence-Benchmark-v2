def composite_nums_between_indices(numbers):
    composite_set = set()

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = min(222, len(numbers) - 1)
    end_index = min(222, len(numbers) - 1)
    for i in range(start_index, end_index + 1):
        if is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set