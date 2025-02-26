def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    result_set = set()
    for index in range(333, 369):
        if index < len(numbers):
            num = numbers[index]
            if is_composite(num):
                result_set.add(num)
    return result_set