def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 22
    end_index = 88
    valid_range = numbers[start_index:end_index + 1]
    composite_set = set((num for num in valid_range if is_composite(num)))
    return composite_set