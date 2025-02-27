def composite_nums_between_indices(num_list):

    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if 56 < len(num_list) > 57:
        return set(filter(check_composite, num_list[56:58] + 1))
    else:
        return set()