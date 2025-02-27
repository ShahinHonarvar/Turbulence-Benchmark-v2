def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    filtered_lst = lst[4:5]
    composite_set = set([x for x in filtered_lst if is_composite(x)])
    return composite_set