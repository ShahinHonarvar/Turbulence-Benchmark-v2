def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for i in range(29, 52):
        if is_composite(num_list[i]):
            composite_set.add(num_list[i])
    return composite_set