def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    result = set()
    start_index = 222
    end_index = 222
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and is_composite(numbers[i]):
            result.add(numbers[i])
    return result