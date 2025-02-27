def composite_nums_between_indices(numbers_list):

    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composite_set = set()
    for i in range(3):
        if is_composite(numbers_list[i]):
            composite_set.add(numbers_list[i])
    return composite_set