def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 30
    end_index = 49
    result_set = set()
    for num in numbers[start_index:end_index]:
        if is_composite(num):
            result_set.add(num)
    return result_set