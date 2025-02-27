def composite_nums_between_indices(lst):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
            else:
                return False
        else:
            return False
    comp_set = set()
    for i in range(75, 95):
        if is_composite(lst[i]) and len(comp_set) < 20:
            comp_set.add(lst[i])
    return comp_set