def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 25
    end_index = 60
    sliced_numbers = numbers[start_index:end_index]
    return set(filter(is_composite, sliced_numbers))