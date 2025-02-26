def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 50
    end_index = 55
    slice_length = len(numbers[start_index:end_index])
    if slice_length == 0:
        return set()
    return {num for num in numbers[start_index:end_index] if is_composite(num)}