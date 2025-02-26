def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 51
    end_index = 87
    range_numbers = numbers[start_index:end_index]
    return set(filter(is_composite, range_numbers))