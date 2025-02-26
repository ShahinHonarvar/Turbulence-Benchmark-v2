def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 37
    end_index = 77
    composite_set = set()
    for i in range(start_index, end_index):
        if i < len(numbers) and is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set