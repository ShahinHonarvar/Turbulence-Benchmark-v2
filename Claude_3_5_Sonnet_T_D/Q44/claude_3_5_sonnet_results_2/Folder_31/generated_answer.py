def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start = 56
    end = 67
    sliced_list = numbers[start:end]
    return set(filter(is_composite, sliced_list))