def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 62
    end_index = 99
    result = set()
    for i in range(start_index, min(end_index + 1, len(numbers))):
        if is_composite(numbers[i]):
            result.add(numbers[i])
    return result