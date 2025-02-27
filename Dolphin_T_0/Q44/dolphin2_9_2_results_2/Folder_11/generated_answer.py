def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    start_index = 37
    end_index = 76
    if end_index > len(num_list) or start_index > end_index:
        return set()
    composite_nums_set = set()
    for i in range(start_index, end_index + 1):
        if is_composite(num_list[i]):
            composite_nums_set.add(num_list[i])
    return composite_nums_set