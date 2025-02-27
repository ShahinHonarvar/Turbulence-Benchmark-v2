def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    indices_range = numbers[37:52]
    composite_numbers = {num for num in indices_range if is_composite(num)}
    return composite_numbers