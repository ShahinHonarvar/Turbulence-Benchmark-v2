def composite_nums_between_indices(num_list):

    def is_composite(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return True
            else:
                return False
        else:
            return False
    composite_nums_set = set()
    for i in range(55, 99):
        if is_composite(num_list[i]):
            composite_nums_set.add(num_list[i])
    return composite_nums_set