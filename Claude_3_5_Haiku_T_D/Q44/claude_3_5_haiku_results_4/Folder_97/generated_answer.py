def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composite_set = set()
    for index in range(15, 40):
        if index < len(numbers):
            current_num = numbers[index]
            if is_composite(current_num):
                composite_set.add(current_num)
    return composite_set