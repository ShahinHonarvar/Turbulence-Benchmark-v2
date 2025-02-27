def composite_nums_between_indices(num_list):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composites = set()
    for i in range(8, 10):
        if is_composite(num_list[i]):
            composites.add(num_list[i])
    return composites