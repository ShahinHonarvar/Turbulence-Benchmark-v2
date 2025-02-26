def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 36
    end_index = 47
    range_numbers = numbers[start_index:end_index]
    return set((num for num in range_numbers if is_composite(num)))