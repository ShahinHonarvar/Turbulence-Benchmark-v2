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
    result = set()
    for num in numbers[start_index:end_index]:
        if is_composite(num):
            result.add(num)
    return result