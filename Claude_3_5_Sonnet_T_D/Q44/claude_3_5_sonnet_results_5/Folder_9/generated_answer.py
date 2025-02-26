def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = max(80, 0)
    end_index = min(200, len(numbers) - 1)
    composite_set = set()
    for index in range(start_index, end_index + 1):
        if index < len(numbers) and is_composite(numbers[index]):
            composite_set.add(numbers[index])
    return composite_set