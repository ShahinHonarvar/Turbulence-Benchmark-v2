def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 30
    end_index = 48
    composite_numbers = {num for num in numbers[start_index:end_index + 1] if is_composite(num)}
    return composite_numbers