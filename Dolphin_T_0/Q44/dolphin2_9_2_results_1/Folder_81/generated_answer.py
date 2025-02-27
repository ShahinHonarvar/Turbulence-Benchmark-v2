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
    comp_nums = set()
    for i in range(20, 201):
        if is_composite(num_list[i]):
            comp_nums.add(num_list[i])
    return comp_nums