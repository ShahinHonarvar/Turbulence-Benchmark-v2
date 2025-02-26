def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 29
    end_index = 93
    sliced_numbers = numbers[start_index:end_index + 1]
    composite_set = set()
    for num in sliced_numbers:
        if is_composite(num):
            composite_set.add(num)
    return composite_set